import streamlit as st
from openai import OpenAI
import base64
from food_helper import FoodNames
import requests
import time

api_key = st.secrets['OPENAI_KEY']
google_search_api_key = st.secrets['GOOGLE_SEARCH_API_KEY']
# st.write(option)
client = OpenAI(api_key=api_key)

def find_ingredients(url):
  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "system", "content": "Your role is to scan the foods that are present in the image and tell me what you see."},
      {
          "role": "user",
          "content": [
              { 
                  "type": "text", 
                  "text": "What's in this image?"
              },
              {
                  "type": "image_url",
                  "image_url": {
                      "url" : f"data:image/jpeg;base64,{url}",
                      "detail": "low"
                  }
              }
          ],
      },
      {
          "role": "user",
          "content": "I want you to only return the names of the foods that are present in the image."
      } 
    ],
    temperature=0.5
  )
  
  ingredients = completion.choices[0].message.content
  return ingredients


def meal_suggestion(ingredients = "", level = "", filter_ingredient_string = "", dietary_string = ""):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
          {"role": "system", "content": "You are a meal suggestion bot. With the provided list of ingredients, acting as what the user had for their meals for the day before, suggest multiple meals for the user to eat."},
          
              
          {
              "role": "user",
              "content": f"With these ingredients: {ingredients}, acting as what the user had for their meals for the day before, suggest 2 meals for the user to eat, providing the name, nutritional value and recipe for the meals suggested, ensuring that the meals are at an {level} of difficulty to create or prep. Please do not include these ingredients in the meals: {filter_ingredient_string}. {dietary_string}"
          } 
        ],
        temperature=0.5
      )

    ingredients = completion.choices[0].message.content
    return ingredients

fn = FoodNames()

def encode_image(image_path):
  # with open(image_path, "rb") as image_file:
  #   return base64.b64encode(image_file.read()).decode('utf-8')
    return base64.b64encode(image_path.read()).decode('utf-8')

# ---------------UI-------------------

st.write('How easy do you want your meal to be prepared?')
option_1 = st.checkbox("Easy (I'm busy ;-;)")
option_2 = st.checkbox("Moderate (I can handle it)")
option_3 = st.checkbox("Difficult (Feeling gourmet today)")

dietary_restrictions = st.selectbox(
    "Do you have any dietry restriction?",
        ("Vegetarian", "Vegan", "Halal", "Lactose intolerant", "Gluten intolerant", "None"))

options = st.multiselect(
    "Ingredients you don't want in meal plan", fn.get_food_names())

filter_ingredient_string = ''
for i in options:
    filter_ingredient_string += f"{i}, "

if st.button("Take a picture of your meal"):
    cameraInput = st.camera_input("Take a picture of your meal")

uploaded_file = st.file_uploader("Upload pictures of past meals", accept_multiple_files=True)
if not (option_1 or option_2 or option_3):
    st.write("Please select at least one option.")
    
elif uploaded_file is not None and len(uploaded_file) == 3:
    # st.write("yes")
    # Getting the base64 string
    base64_image0 = encode_image(uploaded_file[0])
    base64_image1 = encode_image(uploaded_file[1])
    base64_image2 = encode_image(uploaded_file[2])
    # image = uploaded_file.read()
    # st.write(image)
    
    st.write("First Meal Ingredients: ")
    ingredients0 = find_ingredients(base64_image0)
    st.write(ingredients0)
    st.write("Second Meal Ingredients: ")
    ingredients1 = find_ingredients(base64_image1)
    st.write(ingredients1)
    st.write("Third Meal Ingredients: ")
    ingredients2 = find_ingredients(base64_image2)
    st.write(ingredients2)


    # ingredients of all 3 images uploaded combined
    all_ingredients = ingredients0 + ingredients1 + ingredients2
    dietary_string = ""

    if dietary_restrictions != "None":
        f"Please return recipes that are suitable for {dietary_restrictions}"

    easy = option_1
    moderate = option_2
    hard = option_3

    is_text = ""

    if is_text == "":
        st.spinner(text="In progress...")
        
    # meal suggestion for easy level
    if easy:    
        st.title("Easier Options")
        easy_meals = meal_suggestion(all_ingredients, "easy", filter_ingredient_string, dietary_string)
        st.write(easy_meals)
        
        is_text += easy_meals

    # meal suggestion for moderate level
    if moderate:
        st.title("Moderate Options")
        moderate_meals = meal_suggestion(all_ingredients, "moderate skill level", filter_ingredient_string, dietary_string)
        st.write(moderate_meals)
        is_text += moderate_meals

    # meal suggestion for hard level
    if hard:
        st.title("Difficult Options")
        hard_meals = meal_suggestion(all_ingredients, "higher skill level", filter_ingredient_string, dietary_string)
        st.write(hard_meals)
        is_text += hard_meals

    


# Web search to obtain links

# def web_search(query):
#     url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={google_search_api_key}&cx={search_engine_id}"
#     response = requests.get(url)
#     results = response.json()
#     return results

# def generate_recipe_links(food):
#     query = f"Recipe for {food}"
#     search_results = web_search(query)
#     recipe_links = [item['link'] for item in search_results.get('items', [])]
#     return recipe_links

