import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening")
def assistant():
    recognizer = sr.Recognizer()
    greet()
    speak("How can I assist you today?")
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio).lower()
            print(f"User: {query}")
            if "wikipedia" in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                speak(f"According to Wikipedia, {result}")
            elif "time" in query:
                current_time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}")
            elif "exit" in query or "stop" in query:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I didn't understand that.")
        except sr.UnknownValueError:
            print("Sorry, I did not hear your request. Please repeat.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
if __name__ == "__main__":
    assistant()
