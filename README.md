# Desktiop_AI-Taraus- The Voice Assistant

Description:
Taraus is a voice assistant program that can perform various tasks such as opening websites, playing music, checking the time, capturing images, and interacting with the OpenAI text model for generating responses to user queries.

Features:
Opens YouTube, Wikipedia, and Google.
Plays music from a specified directory.
Displays the current time.
Captures images using the system's camera.
Opens the VLC Media Player.
Interacts with OpenAI for generating responses to user queries.

Dependencies:
Python 3.x

Libraries: requests, speech_recognition, pyttsx3, datetime, cv2 (OpenCV), webbrowser

Setup:
Install Python 3.x from https://www.python.org/.
Install required libraries using pip:
Copy code
pip install requests SpeechRecognition pyttsx3 opencv-python-headless
Clone or download the project files.

Usage:
Run the script Taraus.py.
Taraus will greet you and listen for commands.
Speak commands such as:
"Open YouTube"
"Open Wikipedia"
"Open Google"
"Open music"
"What's the time?"
"Open camera"
"Show image" or "Display image"
"Play movies"
"Open AI"
"Exit" or "Quit"

Adding New Commands:
To add new commands, you can extend the while True loop in Taraus.py and define functions for the desired tasks.

OpenAI Integration:
Taraus can interact with OpenAI's text model to generate responses to user queries.
Set up your OpenAI API key in the script.
Command Taraus with "Open AI" and then provide a prompt for the task you want to perform.

Contributing:
Feel free to contribute to this project by adding new features, fixing bugs, or improving the existing code. Pull requests are welcome!

Author:
This project is created by Akshat Gupta.
