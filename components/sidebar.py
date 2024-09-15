import streamlit as st
import json
from vertexai.generative_models import GenerationConfig

def sidebar_configuration():
    st.sidebar.header("System Configuration")
    system_instruction = st.sidebar.text_area(
        "Enter system instruction:", value="Enter system instruction here"
    )

    # Sidebar: GenerationConfig parameters
    st.sidebar.header("Generation Config")
    temperature = st.sidebar.number_input("Temperature", min_value=0.0, max_value=1.0, value=0.7)
    top_p = st.sidebar.number_input("Top-p", min_value=0.0, max_value=1.0, value=0.9)
    top_k = st.sidebar.number_input("Top-k", min_value=0, value=40)
    candidate_count = st.sidebar.number_input("Candidate Count", min_value=1, value=1)
    max_output_tokens = st.sidebar.number_input("Max Output Tokens", min_value=1, value=1024)
    stop_sequences_input = st.sidebar.text_input("Stop Sequences (comma-separated)", value="")
    presence_penalty = st.sidebar.slider("Presence Penalty", min_value=-2.0, max_value=2.0, value=0.0, step=0.1)
    frequency_penalty = st.sidebar.slider("Frequency Penalty", min_value=-2.0, max_value=2.0, value=0.0, step=0.1)
    response_mime_type = st.sidebar.selectbox("Response MIME Type", options=["text/plain", "application/json"])
    response_schema_input = st.sidebar.text_area("Response Schema (JSON)", value="")
    seed = st.sidebar.number_input("Seed (0 for None)", min_value=0, value=0)

    # Process stop sequences
    stop_sequences = [s.strip() for s in stop_sequences_input.split(",")] if stop_sequences_input else None

    # Process response schema
    response_schema = None
    if response_schema_input:
        try:
            response_schema = json.loads(response_schema_input)
        except json.JSONDecodeError:
            st.sidebar.error("The response schema must be in valid JSON format.")

    # Define GenerationConfig
    generation_config = GenerationConfig(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        candidate_count=candidate_count,
        max_output_tokens=max_output_tokens,
        stop_sequences=stop_sequences,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
        response_mime_type=response_mime_type,
        response_schema=response_schema,
        seed=seed if seed != 0 else None
    )

    return system_instruction, generation_config
