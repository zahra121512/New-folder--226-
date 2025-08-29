import speech_recognition as sr
import pyttsx3
from datetime import datetime
def  speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak now...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"you said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("sorry, I did not get that")
        except sr.RequestError as e:
            print(f"api error; {e}")
    return ""
def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "your name" in command:
        speak("I am your python voice assistant.")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif "exit" in command or "stop" in command:
        speak("goodbye")
        return False
    else:
        speak(("im not sure if i can help with that"))
    return True
def main():
    speak("voice assistaint activated say something")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break
if __name__ == "__main__":
    main()