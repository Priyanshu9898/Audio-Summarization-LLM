import google.generativeai as genai
import os
from dotenv import load_dotenv
from IPython.display import display
from IPython.display import Markdown
import textwrap
import tempfile
import streamlit as st


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)


def summarize_audio(audio_file_path):

    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    audio_file = genai.upload_file(audio_file_path)

    response = model.generate_content(
        [
            "Please summarize the following audio.",
            audio_file
        ]
    )

    return response.text


def save_uploaded_file(uploaded_file):
    """Save uploaded file to a temporary file and return the path."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    except Exception as e:
        st.error(f"Error handling uploaded file: {e}")
        return None
