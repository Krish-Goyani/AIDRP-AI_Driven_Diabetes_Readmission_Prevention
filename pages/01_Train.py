import streamlit as st
import os
import time

# Set Streamlit page configuration
st.set_page_config(
    page_title="AIDRP",
    page_icon="🧑‍⚕️"
)

# Streamlit header and information
st.header("Model Training", divider="rainbow")
st.write("Press the start button to begin model training. this may take a few minutes based on your device's performance.")

# Check if the start button is clicked
if st.button("Start"):
    # Execute the model training command
    os.system("python main.py")
    
    # Display completion message
    st.write("Model training completed")
