# Whisper Transcription and Translation App

## Project Description
This project is a Streamlit application that utilizes OpenAI's Whisper model for audio transcription and translation. Users can record voice messages, which the application will transcribe into text or translate into another language.

![downloaded transcription](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/69arvtdfjmtgmfkiogbv.png)


## Features
- **Audio Transcription**: Record a voice message and get the transcription in text format.
- **Audio Translation**: Record a voice message and get the translation in text format.
- **Save Transcription**: Option to save the transcribed text to a `.txt` file.

## Requirements
- Python 3.x
- Streamlit
- OpenAI API
- dotenv


## Set up your environment variables:

   - Create a `.env` file in the root directory and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

2. Open your web browser and go to `http://localhost:8501` to access the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
