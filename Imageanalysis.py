import streamlit as st
import google.generativeai as genai
from PIL import Image

### Provide the api key
api_key = "AIzaSyBhND33Sv5KLwqlGYlfGJUxVWbpco1JNOU"
genai.configure(api_key=api_key)

### Choose the heading
st.header('Optical Character Recognition System')

#  Uploder a File
uploaded_file = st.file_uploader('upload an image', type = ['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    st.image(Image.open(uploaded_file))

# what you want to ask
prompt = st.text_input("Enter the text")

# use Gen Ai skills

if st.button("GET RESPONSE"):
    img = Image.open(uploaded_file)
    model=genai.GenerativeModel("gemini-1.0-pro-vision-latest")
    response=model.generate_content([prompt,img])
    st.markdown(response.text)