import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv() 

# Set Streamlit page configuration
st.set_page_config(
    page_title="AIDRP",
    page_icon="🧑‍⚕️")
with st.sidebar:
    st.write("I'm your nutritional ally. Let me test your meal before you eat.")


genai.configure(api_key= os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')
st.header("MealScan🕵️: Your Nutritional Ally",divider='green')
st.write("Upload a photo of your meal to get its overview, sugar content and health rating.")


img = st.file_uploader("Choose an image...")

if img:
    img = Image.open(img)

    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(img.resize((200,200)),caption="Uploaded Image")

    st.write("")
    response = model.generate_content(['''You are a nutritional analysis assistant. Your task is to review the provided food dish/recipe/meal image and respond to the following questions in a clear, structured format it should contains three sections described below:
    Provide a brief overview of the meal depicted in the image.
    Estimate the approximate amount of sugar (in grams) per 100 grams of the depicted meal.
    Rate the overall healthiness of the meal on a scale of 1 to 5, where 1 represents an unhealthy meal and 5 represents an exceptionally nutritious meal. Provide a brief justification for your rating, considering factors such as nutrient density, balance of macronutrients, and the presence of beneficial or harmful components.''', img], stream=True)

    response.resolve()
    st.write("MealScan's report :")
    st.markdown(response.text)


