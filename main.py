import streamlit as st
from openai import OpenAI

api_key = st.secrets['OPENAI_KEY']
# st.write(option)
client = OpenAI(api_key=api_key)

def story_ai(prompt):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
      'role': 'system',
      'content': 'Based on the story given, you will deisgn a detailed image prompt for the cover of this story. the image prompt should include the theme of the story with relevant color, suitable for adults. The output should be within 500 characters.'
    }, {
      "role": "user",
      "content": prompt
    }],
    temperature=0.8
  )
  story = response.choices[0].message.content
  return story

   
msg = st.text_input(label='Keywords to generate a story')

story = story_ai(msg)

st.write(story)