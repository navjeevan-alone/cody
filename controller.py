# controller.py

import model
import view

class Controller:
    def __init__(self, query_list):
        self.model = model.Model(query_list)
        self.view = view.View()
        self.listening = False

    def listen_loop(self):
        while self.listening:
            query = self.model.take_command().lower()
            function = self.model.find_best_match(query)
            if function is not None:
                eval(function)
            else:
                self.view.update_label("No matching command found")

    def run(self):
        self.view.run()

    def button_clicked(self):
        self.start_stop_listening()

if __name__ == "__main__":
    query_list = [
        {"command": "test", "function": "test()"},
        {"command": "wikipedia", "function": "search_wikipedia()"},
        {"command": "search on youtube", "function": "search_youtube()"},
        # Add more commands as needed
    ]
    controller = Controller(query_list)
    controller.run()
