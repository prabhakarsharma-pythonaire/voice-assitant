# Voice Assistant using Google Generative AI and Speech Recognition

## Overview

This project is a voice assistant application that leverages Google's Generative AI (Gemini model) and the `speech_recognition` library to process speech input and generate contextually appropriate responses. The assistant can listen to user queries, process them using an advanced language model, and respond with natural-sounding speech.

## Features

- **Speech-to-Text**: Converts spoken language into text using the `speech_recognition` library.
- **Language Processing**: Processes the converted text using Google's Gemini language model to generate a contextually relevant response.
- **Text-to-Speech**: Converts the response text into speech using `gTTS` (Google Text-to-Speech).
- **User Interface**: Provides a simple graphical user interface using `tkinter` for interaction, with buttons to start/stop listening and exit the application.
- **Continuous Listening**: Once started, the assistant continuously listens for input until the user decides to stop it.
- **Customizable Behavior**: The assistant can be customized for specific tasks, including setting response styles or integrating with other services.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- The following Python packages:
  - `google-generativeai`
  - `speechrecognition`
  - `gtts`
  - `playsound`
  - `tkinter` (usually comes pre-installed with Python)
  
Install the required packages via pip:

```bash
pip install google-generativeai SpeechRecognition gtts playsound


##clone repo
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
Replace the placeholder GOOGLE_API_KEY in logic_imp.py with your actual Google API key.

#run application
python voice_assistant_ui.py

