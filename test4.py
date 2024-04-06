import tkinter as tk

class ToggleButton(tk.Canvas):
    def __init__(self, master, size=50, **kwargs):
        super().__init__(master, width=size, height=size, bd=0, highlightthickness=0, **kwargs)
        self.size = size
        self.current_shape = 'circle'
        self.draw_button()

    def draw_button(self):
        self.delete("all")  # Clear the canvas before redrawing
        # Draw the triangle border
        self.create_polygon(0, self.size, self.size, self.size, self.size / 2, 0, fill='', outline='black', width=2)
        # Draw the circle or square inside based on the current shape
        if self.current_shape == 'circle':
            self.create_oval(10, 10, self.size - 10, self.size - 10, fill='blue', outline='')
        else:
            self.create_rectangle(10, 10, self.size - 10, self.size - 10, fill='blue', outline='')
    
    def toggle_shape(self):
        self.current_shape = 'square' if self.current_shape == 'circle' else 'circle'
        self.draw_button()

def toggle_shape():
    button.toggle_shape()

root = tk.Tk()
root.geometry("200x200")

button = ToggleButton(root, size=100)
button.pack(pady=20)

toggle_button = tk.Button(root, text="Toggle Shape", command=toggle_shape)
toggle_button.pack()

root.mainloop()
