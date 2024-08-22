import dearpygui.dearpygui as dpg
import threading
from logic_imp import audio_to_text, chat_with_gemini, text_to_speech, play_audio

audio_file_path = "response.mp3"
is_listening = False

def start_continuous_listening():
    global is_listening
    is_listening = True
    dpg.set_value("text_display", "Listening continuously...")
    threading.Thread(target=continuous_listening).start()

def stop_listening():
    global is_listening
    is_listening = False
    dpg.set_value("text_display", "Listening stopped.")

def continuous_listening():
    while is_listening:
        prompt = audio_to_text()
        if prompt:
            dpg.set_value("text_display", f"Recognized: {prompt}")
            response = chat_with_gemini(prompt)
            dpg.set_value("text_display", f"Gemini: {response}")
            text_to_speech(response, audio_file_path)
            play_audio(audio_file_path)

def ui_setup():
    with dpg.window(label="Voice Assistant", width=600, height=400):
        dpg.add_text("Ready to chat...", tag="text_display")
        dpg.add_button(label="Start Continuous Listening", callback=start_continuous_listening)
        dpg.add_button(label="Stop Listening", callback=stop_listening)

    dpg.create_viewport(title="Voice Assistant", width=600, height=400)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    dpg.create_context()
    ui_setup()
