import streamlit as st
from src.helper import summarize_audio, save_uploaded_file

# Streamlit app interface
st.title('Audio Summarization App')

with st.expander("About this app"):
    st.write("""
        This app uses Google's generative AI to summarize audio files. 
        Upload your audio file in WAV or MP3 format and get a concise summary of its content.
    """)

audio_file = st.file_uploader("Upload Audio File", type=['wav', 'mp3'])
if audio_file is not None:
    # Save the uploaded file and get the path
    audio_path = save_uploaded_file(audio_file)
    st.audio(audio_path)

    if st.button('Summarize Audio'):
        with st.spinner('Summarizing...'):
            summary_text = summarize_audio(audio_path)
            st.info(summary_text)
