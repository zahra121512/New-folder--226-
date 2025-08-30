import speech_recognition as sr
import pyttsx3
from datetime import datetime
def  speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
def get_audio():
    """
    Listens for audio input from the microphone and returns the recognized text.
    """
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Speak now...")
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
            try:
                command = r.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
            except sr.UnknownValueError:
                print("Sorry, I did not get that. Please try again🧏🏼‍♀️.")
                speak("Sorry, I did not get that. Please try again.🧏🏼‍♀️")
            except sr.RequestError:
                print("Sorry, there was a problem with the speech recognition service🎙️.")
                speak("Sorry, there was a problem with the speech recognition service.🎙️")
    except Exception as e:
        print(f"Microphone error:🎙️ {e}")
        speak("Sorry, I could not access the microphone.🎙️")
    return None
def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today? You can ask me about the time, date, or my name or just say goodbye to exit if you want😁")
    elif "your name" in command or "who are you" in command:
        speak("I am your Python voice assistant, created to help you with simple tasks.")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}.")
    elif "date" in command:
        today = datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {today}.")
    elif "exit" in command or "quit" in command or "goodbye" in command:
        speak("Goodbye! Have a great day.")
        return False
    else:
        speak("Sorry, I didn't understand that😔. Please try again.😅")
    return True

def main():
    """
    Main function to activate the voice assistant and process user commands.
    """
    speak("Voice assistant activated. Say something when you're ready.🫡")
    while True:
        command = get_audio()
        if command:
            if not respond_to_command(command):
                break
        else:
            print("good bye...👋🏼")


            if __name__ == "__main__":
                main()