import streamlit as st
from config import Config
from vertexai.generative_models import Part
from models.generative_model_wrapper import GenerativeModelWrapper
from utils.session_state import init_session_state
from components.sidebar import sidebar_configuration
from components.file_upload import file_upload_section
from components.uri_input import uri_input_section
from components.chat_input import chat_input_section
from components.conversation_history import display_conversation_history

def main():
    st.set_page_config(page_title="いのりんの箱", page_icon="🚀", layout="wide")
    st.title("Vertex AI Multimodal Generative Model")

    # Initialize session state
    init_session_state()

    # Sidebar configuration
    system_instruction, generation_config = sidebar_configuration()

    # Update or create the model wrapper
    if "model_wrapper" not in st.session_state:
        st.session_state.model_wrapper = GenerativeModelWrapper(system_instruction)
    else:
        st.session_state.model_wrapper.system_instruction = system_instruction

    st.session_state.generation_config = generation_config

    # Top section: File upload and URI input
    contents = []
    contents += file_upload_section()
    contents += uri_input_section()

    # Chat input section
    user_input = chat_input_section()
    if user_input:
        contents.append(user_input)

    # Generate response
    if st.button("Send Message"):
        if contents:
            # Build the full contents with conversation history
            history_parts = []
            for idx, message in enumerate(st.session_state.conversation_history):
                if idx % 2 == 0:
                    # User message
                    history_parts.append(Part.from_text(message))
                else:
                    # AI response
                    history_parts.append(Part.from_text(message))

            full_contents = history_parts + contents

            with st.spinner("Generating response..."):
                try:
                    response_text = st.session_state.model_wrapper.generate_content(
                        contents=full_contents,
                        generation_config=st.session_state.generation_config
                    )
                    st.success("Response generated!")
                    # Update conversation history
                    user_inputs = []
                    for part in contents:
                        if hasattr(part, 'text') and part.text:
                            user_inputs.append(part.text)
                    st.session_state.conversation_history.extend(user_inputs)
                    st.session_state.conversation_history.append(response_text)

                    # Clear contents for next input
                    contents.clear()
                    # Optionally, clear URI inputs
                    st.session_state.uri_list.clear()
                except Exception as e:
                    st.error(f"An error occurred during generation: {e}")
        else:
            st.error("Please provide content before sending the message.")


    # Display conversation history
    display_conversation_history()

    # Clear all history button
    if st.button("Clear All History"):
        st.session_state.conversation_history.clear()
        st.success("All conversation history has been cleared.")

if __name__ == "__main__":
    main()
