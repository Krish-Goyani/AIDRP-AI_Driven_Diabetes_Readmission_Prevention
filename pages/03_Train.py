import streamlit as st
import os
import time

st.set_page_config(
    page_title="AIDRP",
    page_icon="🧑‍⚕️")

st.header("Model Training",divider="rainbow")
st.write("Press start Button to start model training this may take few minutes based on your device's performance.")

if st.button("Start"):
    os.system("python main.py")
    st.write("Model training completed")
    