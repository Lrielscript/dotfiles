import tkinter as tk

# Variable constants
FULLSCREEN = "-fullscreen"
TOPMOST = "-topmost"
BACKGROUND_COLOR = "black"
CURSOR_STYLE = "none"
EXIT_KEY = "<Escape>"

def close_window(event=None):
    root.destroy()

# Main Window
root = tk.Tk()

# Window configuration
root.attributes(FULLSCREEN, True)
root.attributes(TOPMOST, True)
root.configure(bg=BACKGROUND_COLOR)
root.config(cursor=CURSOR_STYLE)

# Emergency Exit Keybinding
root.bind(EXIT_KEY, close_window)

# Start
root.mainloop()
