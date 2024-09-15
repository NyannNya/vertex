import streamlit as st

def display_conversation_history():
    if st.session_state.conversation_history:
        st.subheader("Conversation History")
        for idx, message in enumerate(st.session_state.conversation_history):
            if idx % 2 == 0:
                # User message
                st.markdown(
                    f"""
                    <div style="background-color: #DCF8C6; color: black; padding: 10px; border-radius: 5px;">
                        <strong>You:</strong><br>{message}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                # AI response
                st.markdown(
                    f"""
                    <div style="background-color: #E6E6E6; color: black; padding: 10px; border-radius: 5px;">
                        <strong>Vertex AI:</strong><br>{message}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            st.markdown("<br>", unsafe_allow_html=True)
