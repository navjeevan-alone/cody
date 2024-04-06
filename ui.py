from queryList import queryList
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as kit
import pyautogui
import sys
import tkinter as tk
import threading
import os
import random
import cv2 
import requests
import time
from difflib import get_close_matches
# from ui import speak,takeCommand 

def search_wikipedia():
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)

def search_youtube():
    query = query.replace("search on youtube", "")
    webbrowser.open(f"www.youtube.com/results?search_query={query}")

def open_youtube():
    speak("What would you like to watch?")
    query = takeCommand().lower()
    kit.playonyt(f"{query}")

def close_chrome():
    os.system("taskkill /f /im chrome.exe")

def close_youtube():
    os.system("taskkill /f /im msedge.exe")

def open_google():
    try:
        speak("What should I search?")
        qry = takeCommand().lower()
        webbrowser.open(f"{qry}")
        results = wikipedia.summary(qry, sentences=2)
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

def close_music():
    os.system("taskkill /f /im vlc.exe")

def get_current_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")

def shutdown_system():
    os.system("shutdown /s /t 5")

def restart_system():
    os.system("shutdown /r /t 5")

def lock_system():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def open_notepad():
    npath = "C:\WINDOWS\system32\\notepad.exe"
    os.startfile(npath)

def close_notepad():
    os.system("taskkill /f /im notepad.exe")

def open_command_prompt():
    os.system("start cmd")

def close_command_prompt():
    os.system("taskkill /f /im cmd.exe")

def open_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        k = cv2.waitKey(50)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWndows()

def go_to_sleep():
    speak('Alright then, I am switching off')
    sys.exit()

def take_screenshot():
    speak('Tell me a name for the file')
    name = takeCommand().lower()
    time.sleep(3)
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    speak("Screenshot saved")
 
def check_ip_address():
    speak("Checking")
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        print(ipAdd)
        speak("Your IP address is")
        speak(ipAdd)
    except Exception as e:
        speak("Network is weak, please try again later")

def increase_volume():
    for i in range(20):
        pyautogui.press("volumeup")

def decrease_volume():
    for i in range(20):
        pyautogui.press("volumedown")

def mute_volume():
    pyautogui.press("volumemute")

def refresh_screen():
    pyautogui.moveTo(1551,551, 2)
    pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
    pyautogui.moveTo(1620,667, 1)
    pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')

def scroll_down():
    pyautogui.scroll(1000)

def drag_visual_studio():
    pyautogui.moveTo(46, 31, 2)
    pyautogui.dragRel(1857, 31, 2)

def draw_rectangular_spiral():
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.write('paint')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.moveTo(100, 193, 1)
    pyautogui.rightClick
    pyautogui.click()
    distance = 300
    while distance > 0:
        pyautogui.dragRel(distance, 0, 0.1, button="left")
        distance = distance - 10
        pyautogui.dragRel(0, distance, 0.1, button="left")
        pyautogui.dragRel(-distance, 0, 0.1, button="left")
        distance = distance - 10
        pyautogui.dragRel(0, -distance, 0.1, button="left")

def close_paint():
    os.system("taskkill /f /im mspaint.exe")

def introduce():
    print('My Name Is Cody')
    speak('My Name Is Cody')
    print('I can Do Everything that my creator programmed me to do')
    speak('I can Do Everything that my god has assigned me to do ')

def creator():
    print('I am created by God, His name is Navjeevan, He used python cobara and vs code')
    speak('I am created by God, His name is Navjeevan, He used python cobara and vs code')

def write_channel_name():
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write("How To Manual", interval=0.1)

def subscribe_channel():
    print("Everyone Who are watching This, Please Subscribe Our Channel How To Manual for Interesting tutorials and information, Thanks For Watching")
    speak("Everyone Who are watching This, Please Subscribe Our Channel How To Manual for Interesting tutorials and information, Thanks For Watching")

def type_text():
    query = query.replace("type", "")
    pyautogui.write(f"{query}")

def open_chrome():
    os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')

def maximize_window():
    pyautogui.hotkey('alt', 'space')
    time.sleep(1)
    pyautogui.press('x')

def google_search(): 
    query = query.replace("google search", "")
    pyautogui.hotkey('alt', 'd')
    pyautogui.write(f"{query}", 0.1)
    pyautogui.press('enter')

def youtube_search():
    query = query.replace("youtube search", "")
    pyautogui.hotkey('alt', 'd')
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(f"{query}", 0.1)
    pyautogui.press('enter')

def open_new_window():
    pyautogui.hotkey('ctrl', 'n')

def open_incognito_window():
    pyautogui.hotkey('ctrl', 'shift', 'n')

def minimize_window():
    pyautogui.hotkey('alt', 'space')
    time.sleep(1)
    pyautogui.press('n')

def open_history():
    pyautogui.hotkey('ctrl', 'h')

def open_downloads():
    pyautogui.hotkey('ctrl', 'j')

def previous_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')

def next_tab():
    pyautogui.hotkey('ctrl', 'tab')

def close_tab():
    pyautogui.hotkey('ctrl', 'w')

def close_window():
    pyautogui.hotkey('ctrl', 'shift', 'w')

def clear_browsing_history():
    pyautogui.hotkey('ctrl', 'shift', 'delete')

def close_chrome():
    os.system("taskkill /f /im chrome.exe")


# Command action functions
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 24:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hi,Navjeevan what  can I do for you?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# GUI setup
def set_gui():
    global root, label, button
    root = tk.Tk()
    root.title("Voice Assistant")
    root.geometry("400x200")

    label = tk.Label(root, text="Listening...")
    label.pack()

    button = tk.Button(root, text="Start/Stop", command=toggle_listening)
    button.pack()
    toggle_listening()  # Start listening by default

    root.mainloop()

def update_label(text):
    label.config(text=text)

def toggle_listening():
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
    wishMe()
    print("Started Listening :)")
    while listening:
        query = takeCommand().lower()
        action = find_best_match(query)
        print(action)
        if action is not None:
            eval(action)
        else:
            print("No matching command or action found.")
        time.sleep(max(2, len(query) // 5))
    print("Stopped Listening :(")  # Optional: Print a message when listening stops

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

def find_best_match(input_str, array_of_objects=queryList):
    commands = [obj['command'] for obj in array_of_objects]
    matches = get_close_matches(input_str, commands)
    if matches:
        best_match = matches[0]
        index = commands.index(best_match)
        return array_of_objects[index]['action']
    else:
        return None  # No match found



def test():
    print("test success")

def toggle_listening():
    global listening
    if not listening:
        listening = True
        update_label("Listening...")
        thread = threading.Thread(target=listen_loop)
        thread.start()
        
    else:
        listening = False
        update_label("Stopped Listening")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

if __name__ == "__main__":
    # engine = setEngine()
    listening =False
    set_gui()


