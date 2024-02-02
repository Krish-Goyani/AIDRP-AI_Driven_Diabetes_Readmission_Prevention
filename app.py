import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="AIDRP",
    page_icon="🧑‍⚕️",
    layout="wide")
st.title('AIDRP - AI-Driven Diabetes Readmission Prevention')

with st.sidebar:
    st.write('\n')
    st.write("Let's leverage the power of AI 🤖 to provide better healthcare 🩺 and utilize resources 🌍 to make one step forward in achieving UN's Sustainable Development Goals 🌱")
logo = Image.open('static/logo.jpg')

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(logo)


st.header('Reducing Readmissions, Improving Care',divider='rainbow')

st.write("""
Hospital readmissions for diabetes patients are a major problem, leading to worse outcomes, higher costs, and wasted resources.  
AIDRP leverages AI to accurately predict and prevent 30-day readmissions for diabetes patients.
""")

st.header('How it Works',divider='rainbow')

st.write("""
Our model is trained on real-world electronic health record (EHR)  data from the U.S. Health Facts Medical Database, which contains medical records  for 100,244 diabetes patients  from 1999 to 2008.  

This allows our AI to:

- Identify patients at high risk of readmission ⚠️
- Target interventions and resources to avoid readmissions ♻️

This AI-enabled solution has the potential to:

- Significantly enhance outcomes and decrease costs for both diabetes patients and healthcare institutions 
- Reduce medical waste production 
- Provide quality health to all 

""")

st.header('Who Can Benefit',divider='rainbow')

st.write("""
- Diabetic patients
- Hospital administrators
- Healthcare providers (doctors, nurses, care coordinators)
- Population health management teams
- Healthcare payers/insurance companies
""")

st.header('Contact Us',divider='rainbow')

st.write("""
To learn more about AIDRP and how it can help your organization, please reach out:

info@aidrp.ai

1992, Patel Boarding
""")
