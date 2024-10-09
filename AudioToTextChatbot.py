# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import streamlit as st
import assemblyai as aai

st.title("AudioToTextChatBot")
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "mp4", "m4a"])
# audio_file = C:\Users\vrish\Documents\Sound recordings\Recording - Copy.mp3


# Replace with your API key
aai.settings.api_key = st.secrest['ASSEMBLY_API_Key']

# URL of the file to transcribe
# FILE_URL = "https://assembly.ai/wildfires.mp3"



# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(audio_file)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    # print(transcript.text)
    st.write("Transcribed Text:")
    st.write(transcript.text)

