# view.py
import controller
import tkinter as tk

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Voice Assistant")
        self.root.geometry("400x200")

        self.label = tk.Label(self.root, text="Listening...")
        self.label.pack()

        self.button = tk.Button(self.root, text="Start/Stop Listening", command=self.start_stop_listening)
        self.button.pack()

    def start_stop_listening(self):
        if controller.listening:
            controller.listening = False
            self.update_label("Stopped Listening")
        else:
            controller.listening = True
            self.update_label("Listening...")
            controller.listen_loop()

    def update_label(self, text):
        self.label.config(text=text)

    def run(self):
        self.root.mainloop()
