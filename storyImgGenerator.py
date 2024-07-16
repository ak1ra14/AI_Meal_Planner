import streamlit as st
from openai import OpenAI
import requests
# st.markdown('**bold**, *Italic*')

def download_image(url, filename):
  response = requests.get(url)
  if response.status_code == 200:
      with open(filename, 'wb') as f:
          f.write(response.content)
      print(f"Image successfully downloaded and saved as {filename}")
  else:
      print(f"Failed to download image. Status code: {response.status_code}")
# if st.button('Hi'):
#   st.write('oi')
#   st.balloons()
#   st.snow()

# option = st.selectbox('What food would you like?', ['Pizza', 'Burger', 'Fries'])
api_key = st.secrets['OPENAI_KEY']
# st.write(option)
client = OpenAI(api_key=api_key)

prompt = st.text_input('Movie prompt', '')

# prompt = ''

if st.button("generate cover"):
  design_response = client.chat.completions.create(
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

  story = design_response.choices[0].message.content
  # st.write(story)

  response = client.images.generate(
    model='dall-e-2',
    prompt = f"{story}",
    size = '256x256',
    quality='standard',
    n=1
    )
  image_url = response.data[0].url
  # return image_url
  url = image_url
  filename = "story.png"
  if image_url:
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image successfully downloaded and saved as {filename}")
        st.write(story)
        st.image(filename)
    
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

  else:
    print("No image URL found.")

  