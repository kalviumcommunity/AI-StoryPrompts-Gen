# app.py
import streamlit as st
from src.groq_client import (
    get_ai_response,
    build_zero_shot_prompt,
    build_one_shot_prompt,
    build_multi_shot_prompt
)
from src.utils import format_ai_output

# Streamlit page config
st.set_page_config(
    page_title="AI Story Prompt Generator",
    page_icon=":sparkles:",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("Project Info")
    st.markdown("""
    **AI Story Prompt Generator**  
    Generate creative story prompts to inspire writers or artists.
    """)
    st.markdown("---")
    st.subheader("Sample Topics / Test Inputs")
    st.markdown("""
    - Fantasy adventure with dragons  
    - Sci-fi space exploration  
    - Romantic story in a futuristic city  
    - Horror short story ideas  
    - Children's bedtime stories  
    """)
    st.markdown("---")
    st.subheader("Prompt Type")
    prompt_type = st.radio("Choose Prompt Type:", [
                           "Zero-Shot", "One-Shot", "Multi-Shot"])
    st.markdown("---")
    st.subheader("Streaming Mode")
    stream_mode = st.checkbox("Enable Streaming Output", value=True)

# Main
st.title("AI Story Prompt Generator")
st.write("Enter a topic or theme to generate creative story prompts!")

topic = st.text_input("Enter your topic or theme:")
submit = st.button("Generate Prompts")

if submit and topic.strip():
    if prompt_type == "Zero-Shot":
        prompt = build_zero_shot_prompt(topic)
    elif prompt_type == "One-Shot":
        prompt = build_one_shot_prompt(topic)
    else:
        prompt = build_multi_shot_prompt(topic)

    with st.spinner("Generating prompts..."):
        ai_response = get_ai_response(prompt, stream=stream_mode)
        formatted_response = format_ai_output(ai_response)

    # Display nicely as numbered list
    st.markdown("**Generated Story Prompts:**")
    prompts = [p.strip() for p in formatted_response.split("\n") if p.strip()]
    for i, p in enumerate(prompts, 1):
        st.write(f"{i}. {p}")
