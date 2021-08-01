"""Escape closes Window

   stevepython.wordpress.com
   code-snippet-vol_42-snip_209

source: Unknown
"""

from tkinter import Tk

def esc_win(event):
    """Destroy root window when escape key pressed."""
    root.destroy()

root = Tk()
root.title('Press ESC')

root.bind('<Escape>', esc_win)
root.focus()

root.mainloop()
