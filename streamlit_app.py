import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()

st.logo(
  "logo.png",
  size="medium",
  link="https://platform.openai.com/docs",
)

st.title("Transcription with Whisper")

audio_value = st.audio_input("record a voice message to transcribe")

if audio_value:
  transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file = audio_value
  )

  transcript_text = transcript.text
  st.write(transcript_text)


  txt_file = "transcription.txt"

  # Initialize session state for download confirmation
  if "downloaded" not in st.session_state:
        st.session_state.downloaded = False

    # Download button
  if st.download_button(
       label="Download Transcription",
       file_name="transcription.txt",data=transcript_text,
  ):
       st.session_state.downloaded = True

    # Show success message after download
  if st.session_state.downloaded:
        st.success("Transcription file downloaded successfully!")


# translate audio
st.header("Translation with Whisper", divider="gray")

audio_translate = st.audio_input("record a voice message to translate")

if audio_translate:
  translate = client.audio.translations.create(
    model="whisper-1",
    file=audio_translate
  )

  st.write(translate.text)
