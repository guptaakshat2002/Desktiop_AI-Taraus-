import webbrowser
import requests
import speech_recognition as sr
import os
import pyttsx3
import datetime
import cv2
import openai

openai.api_key = 'sk-AYY47JOFemMxIOmzCfpNT3BlbkFJIgHtlmiR0dqtrvxyn...'  # you have to creat your own key 

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1.0
        print("Listening.... ")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="En-in")
            print(f"User said:{query}")
            return query.lower()
        except Exception as e:
            print("Some error occurred:", str(e))
            return " "


def captureImage():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_image.jpg", frame)
        speak("Image captured and saved as captured_image.jpg")
    else:
        speak("Sorry, unable to capture image.")
    cap.release()
    cv2.destroyAllWindows()


def showImage():
    img_path = "captured_image.jpg"
    if os.path.exists(img_path):
        img = cv2.imread(img_path)
        cv2.imshow("Captured Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        speak("No captured image found.")


def openVLCmediaplayer():
    VLCmediaplayer_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN"
    if os.path.exists(VLCmediaplayer_path):
        os.startfile(VLCmediaplayer_path)
        speak("VLC Media Player is now opened.")
    else:
        speak("VLC Media Player not found.")

def openAI(text):
    try:
        response = requests.post(
             "https://api.openai.com/v1/engines/text-davinci-002/completions",
            headers={
                "Authorization": f"Bearer {'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'}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": text,
                "max_tokens": 100
            }
        )
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['text'].strip()
        else:
            print("Error:", response.text)
            return "Error occurred while processing your request."
    except Exception as e:
        print("Error:", e)
        return "Error occurred while processing your request."
def printToTextEditor(text):
    with open("openai_response.txt", "w") as file:
        file.write(text)
    os.startfile("openai_response.txt")




if __name__ == '__main__':
    speak("Hello, I am Taraus, your assistant. How can I help you?")
    while True:
        query = takeCommand()

        if "open youtube" in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif "open wikipedia" in query:
            speak("Opening Wikipedia...")
            webbrowser.open("https://www.wikipedia.org")

        elif "open google" in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif "open music" in query:
            speak("Opening music...")
            music_path = r"C:\Users\ASUS\Downloads\sonf.mp3"
            os.startfile(music_path)

        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif "open camera" in query:
            speak("Opening camera...")
            captureImage()

        elif "show image" in query or "display image" in query:
            speak("Showing captured image...")
            showImage()

        elif "play movies" in query:
            speak("Opening VLC Media Player location...")
            openVLCmediaplayer()

        elif "open ai" in query:
            speak("What task do you want me to perform?")
            prompt = takeCommand()
            if prompt:
                speak("Let me assist you with that.")
                response = openAI(prompt)
                speak("Here is the response from OpenAI.")
                printToTextEditor(response)
            else:
                speak("Sorry, I couldn't understand the task.")

        elif "exit" in query or "quit" in query:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I couldn't understand the command.")

