import os
import subprocess
import speech_recognition as sr
from pydub import AudioSegment
import streamlit as st
import time

# Explicitly set the ffmpeg path
AudioSegment.ffmpeg = "C:/ffmpeg/bin/ffmpeg.exe"
AudioSegment.ffprobe = "C:/ffmpeg/bin/ffprobe.exe"

# Function to convert MP3 to WAV
def convert_mp3_to_wav(mp3_file, wav_file):
    """Converts an MP3 file to WAV format using FFmpeg."""
    try:
        subprocess.run(['C:/ffmpeg/bin/ffmpeg.exe', '-i', mp3_file, wav_file], check=True)
        return wav_file
    except subprocess.CalledProcessError as e:
        st.error(f"Error converting MP3 to WAV: {e}")
        return None
    except FileNotFoundError:
        st.error("FFmpeg not found. Make sure it's installed and in your PATH.")
        return None

# Function to transcribe audio to text using Google Web Speech API
def transcribe_audio(audio_file_path, language="uz-UZ"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language=language)
        return text
    except sr.UnknownValueError:
        st.error("Google Speech Recognition could not understand the audio.")
        return None
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Streamlit App
# Streamlit App
def save_transcription_as_text(transcription, filename="transcription.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(transcription)
        return filename
    except Exception as e:
        st.error(f"Error saving transcription: {e}")
        return None
def main():
    # Set page title and icon
    st.set_page_config(page_title="MP3 to Uzbek Text Transcription", page_icon="🎤")
    
    # Add custom CSS to style the app
    st.markdown("""
    <style>
        .title {
            font-size: 40px;
            color: #ff6347;
            font-weight: bold;
        }
        .text {
            font-size: 18px;
            color: #4b0082;
        }
        .footer {
            font-size: 14px;
            text-align: center;
            color: #555;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="title">MP3 to Uzbek Text Transcription</p>', unsafe_allow_html=True)
    st.markdown('<p class="text">Upload an MP3 file, and the app will transcribe it to text in Uzbek.</p>', unsafe_allow_html=True)

    # Image or Animation (Uzbek-related)
    # Replace the URL below with a GIF related to Uzbekistan
    st.image("https://img.freepik.com/free-photo/uzbekistan-national-flag-isolated-3d-white-background_1379-497.jpg", width=400)

    # File uploader
    uploaded_file = st.file_uploader("Upload an MP3 file", type=["mp3"], key="file_uploader")
    
    if uploaded_file is not None:
        # Save the uploaded MP3 file to the current directory
        mp3_path = os.path.join(os.getcwd(), uploaded_file.name)
        with open(mp3_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Show an animation while processing
        with st.spinner('Converting MP3 to WAV and transcribing...'):
            time.sleep(2)  # Simulate processing time

        # Convert MP3 to WAV
        wav_path = mp3_path.replace(".mp3", ".wav")
        wav_file = convert_mp3_to_wav(mp3_path, wav_path)

        if wav_file:
            # Transcribe the WAV file to text
            transcription = transcribe_audio(wav_file, language="uz-UZ")
            if transcription:
                st.subheader("Transcription:")
                st.write(transcription)
                text_file = save_transcription_as_text(transcription)
                if text_file:
                    with open(text_file, "r", encoding="utf-8") as file:
                        st.download_button(
                            label="Download Transcription as Text File",
                            data=file,
                            file_name=text_file,
                            mime="text/plain")
            # Clean up files after processing
            if os.path.exists(mp3_path):
                os.remove(mp3_path)
            if os.path.exists(wav_path):
                os.remove(wav_path)

    # Footer
    st.markdown('<p class="footer"> Muhammadjon</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
