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
import tkinter as tk
import threading
from queryList import queryList

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

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        update_label("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        update_label("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        update_label(query)
        return query.lower()
    except Exception as e:
        print("Say that again please...")
        update_label("Say that again please...")
        return "None"

def setEngine(start_engine=True):
    if not start_engine:
        return None
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    return engine

def start_stop_listening():
    global listening
    if listening:
        listening = False
        update_label("Stopped Listening")
    else:
        listening = True
        update_label("Listening...")
        thread = threading.Thread(target=listen_loop)
        thread.start()

def listen_loop():
    while listening:
        query = takeCommand().lower()
        function = find_best_match(query)
        if function is not None:
            eval(function)
        else:
            print("No matching command or function found.")
        time.sleep(max(2, len(query) // 5))

def update_label(text):
    label.config(text=text)

def set_gui():
    global root, label, button
    root = tk.Tk()
    root.title("Voice Assistant")
    root.geometry("400x200")

    label = tk.Label(root, text="Not Listening")
    label.pack()

    button = tk.Button(root, text="Start/Stop", command=start_stop_listening)
    button.pack()

    root.mainloop()

# Define pyttsx3 engine
engine = setEngine()

# GUI setup
if __name__ == "__main__":
    listening =True
    set_gui()
