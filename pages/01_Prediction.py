import streamlit as st


st.set_page_config(
    page_title="AIDRP",
    page_icon="🧑‍⚕️",
    layout="wide")

st.title('Diabetes Readmission Risk Predictor')
with st.form("my_form"):
    st.write("inside")
    st.form_submit_button()
    submitted = st.form_submit_button("Submit")
    if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)
#st.write(f'The risk of 30-day readmission is {pred_prob:.2%}')