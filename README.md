# Uzbek_SpeechToText
![image](https://github.com/user-attachments/assets/8ed0beee-e2dc-4a06-85fd-f8a0b1b35738)

MP3 to Uzbek Text Transcription

![image](https://github.com/user-attachments/assets/db2727ac-6021-43cc-92fe-91b2437ef506)

This project allows users to upload an MP3 file, convert it to a WAV format, and transcribe the audio to text in the Uzbek language using Google's Speech Recognition API. The transcription can be saved as a .txt file and downloaded.

![image](https://github.com/user-attachments/assets/532d2d7c-5551-4507-9f45-3b1e6d942223)

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

![image](https://github.com/user-attachments/assets/3b55e852-d0f4-41d4-9941-2bfbae88d084)


Install FFmpeg:
![image](https://github.com/user-attachments/assets/d6327274-fd3d-45f9-903e-ec8f1029ac15)

Download FFmpeg from FFmpeg official site and extract it.
Set the path to the ffmpeg.exe binary in your script or ensure it’s available in your system’s PATH.
Run the Streamlit app:


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
