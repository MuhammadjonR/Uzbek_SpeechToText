# Uzbek_SpeechToText
MP3 to Uzbek Text Transcription
This project allows users to upload an MP3 file, convert it to a WAV format, and transcribe the audio to text in the Uzbek language using Google's Speech Recognition API. The transcription can be saved as a .txt file and downloaded.

Features:
MP3 to WAV Conversion: Upload an MP3 file, and the app converts it to WAV format.
Transcription: The audio is transcribed into text using the Google Web Speech API.
Downloadable Text File: The transcribed text is available for download as a .txt file.
Streamlit Web App: Built with Streamlit, an easy-to-use framework for creating interactive web applications.
Requirements:
Python 3.x (Tested with Python 3.13)
Libraries:
streamlit: For creating the web app interface.
speech_recognition: For transcribing audio using Google's Web Speech API.
pydub: For handling audio file conversion (MP3 to WAV).
ffmpeg: Required for audio file conversion (ensure it's installed and accessible via the system's PATH).
Installation:
To get started, clone this repository and install the required dependencies.

Clone the repository:

git clone https://github.com/your-username/MP3-to-Uzbek-Text-Transcription.git
cd MP3-to-Uzbek-Text-Transcription

bash

pip install -r requirements.txt
You can create a requirements.txt file with the following contents:


streamlit
speechrecognition
pydub
Install FFmpeg:

Download FFmpeg from FFmpeg official site and extract it.
Set the path to the ffmpeg.exe binary in your script or ensure it’s available in your system’s PATH.
Run the Streamlit app:

bash

streamlit run app.py
Your app will be accessible at http://localhost:8501.

Usage:
Open the app in your browser.
Upload an MP3 file.
The app will convert the MP3 file to WAV and transcribe the audio.
Once the transcription is complete, you can download the transcription as a .txt file.
Example:
Upload an MP3 file containing Uzbek audio.
Wait for the conversion and transcription process to complete.
Download the transcription as a .txt file.
Notes:
Ensure that FFmpeg is correctly installed and configured.
The transcription quality depends on the clarity of the audio and the accuracy of Google's Speech API.
