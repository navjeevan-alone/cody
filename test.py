import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def toggle_listening():
    pass  # Placeholder for the toggle_listening function

def set_gui():
    global root, label, button, close_button
    root = tk.Tk()
    root.wm_attributes('-topmost', True) # always on top
    root.resizable(False, False)  # This disables the window from being resized
    root.overrideredirect(True)  # This removes the window decorations

    root.title("Voice Assistant")
    root.geometry("200x150+100+40")  # Example position, replace with your desired position

    # Load drop shadow image
    shadow_img = Image.open("shadow.png")
    shadow_bg = ImageTk.PhotoImage(shadow_img)

    # Create a label to display the shadow image
    shadow_label = tk.Label(root, image=shadow_bg, bg='black')
    shadow_label.place(x=-10, y=-10, relwidth=1, relheight=1)

    # Function to move the window
    def move_window(event):
        root.geometry(f"+{event.x_root}+{event.y_root}")

    # Bind mouse events for window movement
    root.bind("<B1-Motion>", move_window)

    # Hover effect for the entire window with transition
    def on_enter(event):
        root.configure(bg='blue')  # Change background color on hover with transition
        root.update_idletasks()  # Update the window immediately to show the transition effect

    def on_leave(event):
        root.after(500, lambda: root.configure(bg='#000000'))  # Restore background color after a delay of 0.5 seconds

    root.bind('<Enter>', on_enter)  # Hover effect on enter
    root.bind('<Leave>', on_leave)  # Hover effect on leave

    # Hide close button until hovered over
    close_button = tk.Button(root, text='X', fg='white', command=root.destroy)
    close_button.place(relx=1.0, rely=0, anchor='ne')
    close_button.bind('<Enter>', lambda event: close_button.config(bg='red'))  # Change color on hover
    close_button.bind('<Leave>', lambda event: close_button.config(bg=root['bg']))  # Restore color

    label = tk.Label(root, text="Listening...")
    label.pack(pady=(30, 10))

    button = tk.Button(root, text="Start/Stop", command=toggle_listening)
    button.pack()
    toggle_listening()  # Start listening by default

    root.mainloop()

set_gui()
