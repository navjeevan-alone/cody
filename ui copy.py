import pyttsx3
import speech_recognition as sr
import threading
import time

# Global variable to track the listening state
listening = False

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print("Say that again please...")
        return "None"

def listen_loop():
    global listening
    while listening:
        query = takeCommand()
        # Process the query as needed

def toggle_listening():
    global listening
    if listening:
        listening = False
        print("Listening stopped")
    else:
        listening = True
        # Start the listening loop in a separate thread
        thread = threading.Thread(target=listen_loop)
        thread.start()
        print("Listening started")

def setEngine(start_engine=True):
    if start_engine:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 150)
        return engine
    else:
        return None

def main():
    # Initialize the engine
    engine = setEngine()

    # GUI code goes here
    # For simplicity, let's just have a command line interface
    while True:
        user_input = input("Enter 'start' to begin listening, 'stop' to stop listening, or 'exit' to quit: ")
        if user_input == 'start':
            toggle_listening()
        elif user_input == 'stop':
            toggle_listening()
        elif user_input == 'exit':
            # Stop the engine before exiting
            if engine is not None:
                engine.stop()
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
