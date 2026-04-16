import speech_recognition as sr
import pyttsx3
import ollama
import sys
import pyaudiowpatch as pyaudio

sys.modules["pyaudio"] = pyaudio
engine = pyttsx3.init()
engine.setProperty('rate',170)

def speak(text):
    print("Bot:", text)
    engine.say(text) 
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except:
        return ""


def brain(question):
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": question}
        ]
    )

    return response["message"]["content"]



def main():
    speak("Hey, How can I help you.")
    while True:
        question = listen()
        if question == "":
            continue
        if "exit" in question:
            speak("Goodbye")
            break

        answer = brain(question)
        short_answer = answer[:200]
        speak(short_answer)



main()