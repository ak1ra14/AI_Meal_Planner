import streamlit as st
from openai import OpenAI

api_key = st.secrets['OPENAI_KEY']
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
                      "url" : url,
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


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    image = uploaded_file.read()
    # st.write(image)
    ingredients = find_ingredients(image)

    st.write(ingredients)
    # st.write(ingredients)
# st.write(find_ingredients("https://cdn.britannica.com/55/174255-050-526314B6"))