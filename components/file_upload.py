import streamlit as st
from vertexai.generative_models import Part

def file_upload_section():
    with st.expander("### Upload Files"):
        contents = []
        uploaded_files = st.file_uploader(
            "Multiple and various types supported",
            accept_multiple_files=True
        )
        if uploaded_files:
            for uploaded_file in uploaded_files:
                file_type = uploaded_file.type
                data = uploaded_file.read()
                part = Part.from_data(data=data, mime_type=file_type)
                contents.append(part)
        return contents
