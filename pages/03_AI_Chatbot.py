import streamlit as st
import os
import google.generativeai as genai

st.set_page_config(
    page_title="AIDRP",
    page_icon="🧑‍⚕️")


with st.sidebar:
    st.info("I'm an AI chatbot not a doctor, Always consult your doctor for any medical issues and do not rely solely on information provided here", icon="ℹ️")

# Initialize Gemini-Pro 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Gemini uses 'model' for assistant; Streamlit uses 'assistant'
def role_to_streamlit(role):
  if role == "model":
    return "assistant"
  else:
    return role

st.header(body='🩺Your personal AI doctor! 👩‍⚕️',divider='green')
st.text(body="I'm your healthcare helper powered by Google's most capable AI model- Gemini.🧠")

# Add a Gemini Chat history object to Streamlit session state
if "chat" not in st.session_state:
    st.session_state.chat= model.start_chat(history = [])

if "const" not in st.session_state:
   st.session_state.const="firstrun"

if st.session_state.const == "firstrun":
   st.session_state.const="rerunned"
   st.session_state.chat.send_message("Now you are my AI doctor your job is to give answers of all questions related to heathcare and speciaaly diabetes and in replay of this propmpt only and only  say'Hello i am your AI doctor.'")

# Display chat messages from history above current input box
for message in st.session_state.chat.history[1:]:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)


# Accept user's next message, add to context, resubmit context to Gemini
if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
    # Display user's last message
    st.chat_message("user").markdown(prompt)
    
    # Send user entry to Gemini and read the response
    response = st.session_state.chat.send_message(prompt) 
    
    # Display last 
    with st.chat_message("assistant"):
        st.markdown(response.text)
