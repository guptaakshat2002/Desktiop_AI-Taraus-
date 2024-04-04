import webbrowser
import speech_recognition as sr
import os
import pyttsx3
import openai


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="hi-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            print("Some error occurred:", str(e))
            return "Some error occurred"


if __name__ == '__main__':
    speak("hello i am Taraus your assistant \n"
          "How can i help you")
    while True:
        print("listining.....")
        query = takeCommand()

        if "open" in query:
            opened = False
            for site in ["youtube", "wikipedia", "google"]:
                speak(f"Opening {site}...")
                webbrowser.open(f"https://www.{site}.com")
                break
            else:
                speak("Sorry, I couldn't understand which website to open.")

