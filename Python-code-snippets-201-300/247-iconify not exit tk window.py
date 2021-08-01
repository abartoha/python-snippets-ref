"""247-Iconify not exit Tk window.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

requirements: None.

origin:
Steve Shambles (from Sync It program)
"""
from tkinter import Tk
root = Tk()

# Remove window toolbar.
root.attributes("-toolwindow", 1) # This line is not Linux compatible.

# Iconify window if exit X is hit by user, rather than lose the window.
root.protocol("WM_DELETE_WINDOW", root.iconify)

# You would eventually use: name_of_your_window.destroy() to kill the window.
# In this demo I have just used root for brevity.
root.mainloop()
