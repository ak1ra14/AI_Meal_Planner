from openai import OpenAI
import streamlit as st

api_key = st.secrets['OPENAI_KEY']

class FoodAI:
    def __init__(self, api_key):
        self.openai_api_key = st.secrets['OPENAI_KEY']
        self.google_search_api_key = st.secrets['GOOGLE_SEARCH_API_KEY']
        # st.write(option)
        self.client = OpenAI(api_key=api_key)

    def find_ingredients(self, url):
      completion = self.client.chat.completions.create(
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
    
    
    def meal_suggestion(self, ingredients = "", level = "", filter_ingredient_string = "", dietary_string = "", cuisine_choice = ""):
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
              {"role": "system", "content": "You are a meal suggestion bot. With the provided list of ingredients, acting as what the user had for their meals for the day before, suggest multiple meals for the user to eat."},
    
    
              {
                  "role": "user",
                  "content": f"these ingredients: {ingredients}, are what the user ate recently. suggest 2 meals of the cuisine choice: {cuisine_choice} for the user to eat as a followup to the meals mentioned for the next day, providing the name, nutritional value and recipe for the meals suggested, ensuring that the meals are at an {level} of difficulty to create or prep. Please do not include these ingredients in the meals: {filter_ingredient_string}. Please ensure the meals generated fit the following dietary requirements: {dietary_string}"
              } 
            ],
            temperature=0.5
          )
    
        ingredients = completion.choices[0].message.content
        return ingredients