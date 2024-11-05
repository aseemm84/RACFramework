import streamlit as st
import PyPDF2
from backend import main_prompt
from PIL import Image
import time
import re
import pandas as pd

# Set page config as the first Streamlit command
st.set_page_config(page_title="CV Bullet Points Creator", page_icon="📄", layout = "wide")

# Custom CSS to improve the look and feel
st.markdown(
    """
    <style>
        .stTextInput > div > div > input {
            background-color: #f0f2f6;
        }
        .stTextArea > div > div > textarea {
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns([1, 4])

logo = Image.open("logo.png")
col1.image(logo, width=100)  # Adjust width as needed
col2.title("CV Creator Pro: RAC Framework")

text_string = st.text_area("Enter Your Achievement", height=200)


# Evaluate button
if st.button("Summarize"):
    if text_string is None:
        st.error("Please enter something to Summarize.")
    else:
        if text_string:
                with st.spinner("Summarizing..."):
                    progress_bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.05)  # Simulate processing time
                        progress_bar.progress(i + 1)
                    result = main_prompt(text_string)
                    st.subheader("RAC Framework Result:")
                    st.write(result)
                

st.sidebar.title("About")
st.sidebar.info("""
Welcome to the CV Bullet Point Creator, your expert assistant for crafting a standout resume!

This tool analyzes your achievement against industry best practices, ensuring it meets the highest standards, and convert it to RAC framework bullet points.

Unlock your career potential with a resume that truly reflects your skills and experiences!
""")
linkedin_url = "https://www.linkedin.com/in/aseem-mehrotra/"
st.sidebar.markdown(f'<a href="{linkedin_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" style="height: 30px;"></a>', unsafe_allow_html=True)
