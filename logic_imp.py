import os
import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
import playsound

# Configure the API key
GOOGLE_API_KEY = "AIzaSyD7sJ2MegXGXdRH4KpiBb6K5JcPrLBb5Js"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

def audio_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=3)
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None

def chat_with_gemini(prompt):
    prompt = f"You are a voice assistant and your name is prabhakar voice assitant . Act like voice assitant and just give output as a voice assistant don't add * etc which won't be good while tellinng anything if not necessary: {prompt}"
    try:
        response = model.generate_content(prompt)
        result = ''.join([p.text for p in response.candidates[0].content.parts])
        return result
    except Exception as e:
        return f"An error occurred: {e}"

def text_to_speech(text, audio_file_path):
    tts = gTTS(text=text, lang='en')
    tts.save(audio_file_path)

def play_audio(audio_file_path):
    playsound.playsound(audio_file_path)
