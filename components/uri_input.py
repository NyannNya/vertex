import streamlit as st
from vertexai.generative_models import Part

def uri_input_section():
    contents = []

    # URI input form
    with st.expander("Input URIs"):
        with st.form(key='uri_form'):
            uri_input = st.text_input("Enter the URI:")
            mime_type_options = ["image/jpeg", "image/png", "text/plain", "application/pdf", "audio/mpeg", "video/mp4", "Other"]
            selected_mime_type = st.selectbox("Select MIME Type", options=mime_type_options)
            mime_type = st.text_input("If MIME Type is Other, please enter your MIME type:")

            submit_uri = st.form_submit_button("Add URI")
            st.write("Only URIs that start with 'gs://...' are accepted.\nExample: gs://cloud-samples-data/generative-ai/image/a-man-and-a-dog.png")

        if submit_uri:
            if uri_input and mime_type:
                if not uri_input.startswith("gs://"):
                    st.error("Invalid URI. The URI must start with 'gs://'.")
                else:
                    supported_mime_types = ["image/jpeg", "image/png", "text/plain", "application/pdf", "audio/mpeg", "video/mp4"]
                    if mime_type not in supported_mime_types and selected_mime_type != "Other":
                        st.error("Unsupported MIME type selected.")
                    else:
                        st.session_state.uri_list.append({'uri': uri_input, 'mime_type': mime_type})
                        st.success("URI added.")
            else:
                st.error("Please provide both URI and MIME type.")

    if st.session_state.uri_list:
        with st.expander("List URIs"):
            for idx, uri_entry in enumerate(st.session_state.uri_list):
                col1_uri, col2_uri = st.columns([1, 4])
                with col1_uri:
                    if st.button("Delete", key=f"delete_uri_{idx}"):
                        st.session_state.uri_list.pop(idx)
                with col2_uri:
                    st.write(f"{idx+1}. URI: {uri_entry['uri']}, MIME Type: {uri_entry['mime_type']}")

    # Add URI parts to contents
    for uri_entry in st.session_state.uri_list:
        try:
            part = Part.from_uri(uri=uri_entry['uri'], mime_type=uri_entry['mime_type'])
            contents.append(part)
        except Exception as e:
            st.error(f"Error adding URI {uri_entry['uri']}: {e}")
    return contents
