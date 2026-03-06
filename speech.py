from RealtimeSTT import AudioToTextRecorder
from LLM import pass_to_model
from gtts import gTTS
from playsound import playsound
import os
import asyncio

def record_text():
    if __name__ == '__main__':
        while True:
            recorder = AudioToTextRecorder(
                wakeword_backend="oww",
                openwakeword_model_paths="",
                wake_words="hey jarvis"
            )

            response = pass_to_model(str(recorder.text()))
            yield response
            print(response)

def speak_text(text: str):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")
    

llm_response = record_text()

speak_text(llm_response)