import streamlit as st

def init_session_state():
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []
    if "uri_list" not in st.session_state:
        st.session_state.uri_list = []
