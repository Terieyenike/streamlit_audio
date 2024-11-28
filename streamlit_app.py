import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

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

  st.write(transcript.text)

  # Save the transcript to a .txt file
  if st.button("Save transcription"):
    txt_file = "transcription.txt"

    with open(txt_file, mode='w', encoding='utf-8') as file:
      file.write(f"Transcription:\n{transcript.text}\n")
      file.write("-" * 50 + "\n")

    st.success(f"Transcript saved to {txt_file}")


st.subheader("Translation with Whisper")

audio_translate = st.audio_input("record a voice message to translate")

if audio_translate:
  translate = client.audio.translations.create(
    model="whisper-1",
    file=audio_translate
  )

  st.write(translate.text)
