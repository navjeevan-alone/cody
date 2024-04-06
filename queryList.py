queryList = [
    {"command": "testing", "action": "test()"},
    {"command": "hello", "action": "test()"},
    {"command": "wikipedia", "action": "search_wikipedia()"},
    {"command": "search on youtube", "action": "search_youtube()"},
    {"command": "open youtube", "action": "open_youtube()"},
    {"command": "open chrome", "action": "close_chrome()"},
    {"command": "close chrome", "action": "close_chrome()"},
    {"command": "close youtube", "action": "close_youtube()"},
    {"command": "open google", "action": "open_google()"},
    {"command": "close google", "action": "close_google()"},
    {"command": "play music", "action": "play_music()"},
    {"command": "play iron man movie", "action": "play_movie()"},
    {"command": "close movie", "action": "close_movie()"},
    {"command": "close music", "action": "close_music()"},
    {"command": "time", "action": "get_current_time()"},
    {"command": "shutdown system", "action": "shutdown_system()"},
    {"command": "restart system", "action": "restart_system()"},
    {"command": "lock system", "action": "lock_system()"},
    {"command": "open notepad", "action": "open_notepad()"},
    {"command": "close notepad", "action": "close_notepad()"},
    {"command": "open command prompt", "action": "open_command_prompt()"},
    {"command": "close command prompt", "action": "close_command_prompt()"},
    {"command": "open camera", "action": "open_camera()"},
    {"command": "go to sleep", "action": "go_to_sleep()"},
    {"command": "take screenshot", "action": "take_screenshot()"},
    {"command": "calculate", "action": "calculate()"},
    {"command": "what is my ip address", "action": "check_ip_address()"},
    {"command": "volume up", "action": "increase_volume()"},
    {"command": "volume down", "action": "decrease_volume()"},
    {"command": "mute", "action": "mute_volume()"},
    {"command": "refresh", "action": "refresh_screen()"},
    {"command": "scroll down", "action": "scroll_down()"},
    {"command": "drag visual studio to the right", "action": "drag_visual_studio()"},
    {"command": "rectangular spiral", "action": "draw_rectangular_spiral()"},
    {"command": "close paint", "action": "close_paint()"},
    {"command": "who are you", "action": "introduce()"},
    {"command": "who created you", "action": "creator()"},
    {"command": "open notepad and write my channel name", "action": "write_channel_name()"},
    {"command": "subscribe", "action": "subscribe_channel()"},
    {"command": "type", "action": "type_text()"},
    {"command": "maximize this window", "action": "maximize_window()"},
    {"command": "google search", "action": "google_search()"},
    {"command": "youtube search", "action": "youtube_search()"},
    {"command": "open new window", "action": "open_new_window()"},
    {"command": "open incognito window", "action": "open_incognito_window()"},
    {"command": "minimise this window", "action": "minimize_window()"},
    {"command": "open history", "action": "open_history()"},
    {"command": "open downloads", "action": "open_downloads()"},
    {"command": "previous tab", "action": "previous_tab()"},
    {"command": "next tab", "action": "next_tab()"},
    {"command": "close tab", "action": "close_tab()"},
    {"command": "close window", "action": "close_window()"},
    {"command": "clear browsing history", "action": "clear_browsing_history()"},
]
import tkinter as tk

class TransparentWindow(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self)
        self.overrideredirect(True)  # Remove window decorations
        # self.attributes('-alpha', 0.8)  # Set transparency level (0.0 to 1.0)
        self.configure(bg='blue')  # Set background color (optional)

        # self.geometry('400x300')  # Set window size, replace with your desired size
        self.resizable(False, False)  # Disable window resizing
        print(self.winfo_screenwidth() )
        print(self.winfo_screenheight() )
        # Hide close button until hovered over
        self.close_button = tk.Button(self, text='X', fg='white', command=self.destroy)
        self.close_button.place(relx=1.0, rely=0, anchor='ne')
        self.close_button.bind('<Enter>', lambda event: self.close_button.config(fg='white',bg="red"))  # Change color on hover
        self.close_button.bind('<Leave>', lambda event: self.close_button.config(fg='white',bg=self['bg']))  # Restore color

        self.lift()  # Bring the window to the front
        self.attributes('-topmost', True)  # Keep the window always on top

if __name__ == "__main__":
    app = TransparentWindow()
    app.mainloop()
