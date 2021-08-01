"""Code snippets vol-59
   291-Splash Screen

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
Windows only
splash-logo.png

origin:
https://github.com/israel-dryer/Transparent-Splash-Screen-Tk/blob/master/splash.py
"""
import tkinter as tk

# Create the main window.
root = tk.Tk()

# Disable the window bar.
root.overrideredirect(1)

# Set trasparency and make the window stay on top.
root.attributes('-transparentcolor', 'white', '-topmost', True)

# Set the background image.
psg = tk.PhotoImage(file='splash-logo.png')
tk.Label(root, bg='white', image=psg).pack()

# Move the window to centre.
root.eval('tk::PlaceWindow . Center')

# Schedule the window to close after 4 seconds
root.after(4000, root.destroy)

# run the main loop
root.mainloop()
