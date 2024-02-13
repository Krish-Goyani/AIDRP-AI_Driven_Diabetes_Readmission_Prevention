import streamlit as st
import subprocess


# Set Streamlit page configuration
st.set_page_config(
    page_title="AIDRP",
    page_icon="🧑‍⚕️"
)

# Streamlit header and information
st.header("Model Training", divider="rainbow")
st.write("Initiate the model training process by clicking the 'Start' button. Please be aware that the duration of this training may vary, depending on the performance specifications of your device. Thank you for your patience..")

# Check if the start button is clicked
if st.button("Start"):

    st.write("Magic is happening......")
    # Execute the model training command
    subprocess.run(["python", "main.py"])
    
    # Display completion message
    st.write("Model training completed")
