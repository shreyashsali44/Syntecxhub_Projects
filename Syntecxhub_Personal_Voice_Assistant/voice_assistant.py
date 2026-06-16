import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Text to Speech Engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Speech Recognition
def listen():

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)

            command = command.lower()

            print("You:", command)

            return command

    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")

    except sr.RequestError:
        speak("Speech service unavailable.")

    except Exception as e:
        speak("Microphone error occurred.")

    return ""

# Command Processing
def execute_command(command):

    if "hello" in command:
        speak("Hello, how can I help you?")

    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The current time is {current_time}")

    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")

    elif "open notepad" in command:

        speak("Opening Notepad")

        os.system("notepad")

    elif "search" in command:

        query = command.replace("search", "")

        speak(f"Searching for {query}")

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

    elif "exit" in command or "stop" in command:

        speak("Goodbye")

        return False

    else:

        speak("Command not recognized")

    return True

# Main Program
speak("Personal Voice Assistant Started")

running = True

while running:

    command = listen()

    if command:

        running = execute_command(command)