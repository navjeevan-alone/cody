# model.py

from difflib import get_close_matches
import speech_recognition as sr
import wikipedia

class Model:
    def __init__(self, query_list):
        self.query_list = query_list

    def find_best_match(self, input_str):
        commands = [obj['command'] for obj in self.query_list]
        matches = get_close_matches(input_str, commands)
        if matches:
            best_match = matches[0]
            index = commands.index(best_match)
            return self.query_list[index]['function']
        else:
            return None  # No match found

    def take_command(self):
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
