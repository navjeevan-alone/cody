import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests
import signal
import sys
from difflib import get_close_matches
# from queryList import queryList

queryList = [
    {"command": "test", "function": "test()"},
    {"command": "wikipedia", "function": "search_wikipedia()"},
    {"command": "search on youtube", "function": "search_youtube()"},
    {"command": "open youtube", "function": "open_youtube()"},
    {"command": "close chrome", "function": "close_chrome()"},
    {"command": "open google", "function": "open_google()"},
    {"command": "close google", "function": "close_google()"},
    {"command": "play music", "function": "play_music()"},
    {"command": "play iron man movie", "function": "play_ironman_movie()"},
    {"command": "close movie", "function": "close_movie()"},
    {"command": "time", "function": "get_current_time()"},
    {"command": "shutdown system", "function": "shutdown_system()"},
    {"command": "restart system", "function": "restart_system()"},
    {"command": "lock system", "function": "lock_system()"},
    {"command": "open notepad", "function": "open_notepad()"},
    {"command": "close notepad", "function": "close_notepad()"},
    {"command": "open command prompt", "function": "open_command_prompt()"},
    {"command": "close command prompt", "function": "close_command_prompt()"},
    {"command": "open camera", "function": "open_camera()"},
    {"command": "pc go to sleep", "function": "go_to_sleep()"},
    {"command": "take screenshot", "function": "take_screenshot()"},
    {"command": "calculate", "function": "calculate()"}
]

def test():
    print("test success")
def find_best_match(input_str, array_of_objects=queryList):
    commands = [obj['command'] for obj in array_of_objects]
    matches = get_close_matches(input_str, commands)
    if matches:
        best_match = matches[0]
        index = commands.index(best_match)
        return array_of_objects[index]['function']
    else:
        return None  # No match found

# actions functions
def search_wikipedia():
    speak('Searching Wikipedia...')
    query = takeCommand().replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)

def search_youtube():
    query = takeCommand().replace("search on youtube", "")
    webbrowser.open(f"www.youtube.com/results?search_query={query}")

def open_youtube():
    speak("What would you like to watch?")
    query = takeCommand().lower()
    kit.playonyt(query)

def close_chrome():
    os.system("taskkill /f /im chrome.exe")

def close_youtube():
    os.system("taskkill /f /im msedge.exe")

def open_google():
    try:
        print("hello")
        speak("What should I search?")
        query = takeCommand().lower()
        webbrowser.open(f"{query}")
        results = wikipedia.summary(query, sentences=2)
        speak(results)
    except:
        speak("I am unable to open Google.")

def close_google():
    os.system("taskkill /f /im msedge.exe")

def play_music():
    music_dir = 'C:/Users/navje/Music'
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, random.choice(songs)))

def play_movie():
    npath = "E:\ironman.mkv"
    os.startfile(npath)

def close_movie():
    os.system("taskkill /f /im vlc.exe")

def exit_on_ctrl_c(signal, frame):
    print("\nExiting...")
    sys.exit(0)

def activate_exit_on_ctrl_c():
    signal.signal(signal.SIGINT, exit_on_ctrl_c)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 24:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hi, Sir what  can I do for you?")

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

def get_operator_fn(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        'divided': operator.truediv,
    }[op]

def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

if __name__ == "__main__":
    activate_exit_on_ctrl_c()
    # wishMe()
    print("started")

    while True:
        query = takeCommand().lower()
        # query = "test"
        if "exit" in  query:
            speak("ok sir bye bye")
            break
        function = find_best_match(query)
        if function is not None:
            eval(function)
        else:
            print("No matching command or function found.")
