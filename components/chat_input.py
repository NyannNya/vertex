import streamlit as st
from vertexai.generative_models import Part

def chat_input_section():
    st.subheader("Chat Input")
    text_input = st.text_area("Enter your message:", height=300)
    if text_input:
        return Part.from_text(text_input)
    return None
