"""Code snippets vol-60
   300-Tk focus, mouse, key press detect demo.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
None

Original code here:
https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
Adapted by Steve Shambles
"""
from tkinter import Frame, Tk
root = Tk()


def key(event):
    """Print if what key is pressed to shell, if any."""
    print("Keypress :", repr(event.char))


def mouse_left_clicked(event):
    """Print co-ords of mouse pointer when left mouse button clicked."""
    frame.focus_set()
    print("Mouse left clicked at", event.x, event.y)


def mouse_middle_clicked(event):
    """Print co-ords of mouse pointer when middle mouse button clicked."""
    frame.focus_set()
    print("Mouse middle clicked at", event.x, event.y)


def mouse_right_clicked(event):
    """Print co-ords of mouse pointer when right mouse button clicked."""
    frame.focus_set()
    print("Mouse right clicked at", event.x, event.y)


def mouse_enter(event):
    """Report when mouse enters frame."""
    frame.focus_set()
    print("Mouse has entered frame")


def mouse_leave(event):
    """Report when mouse leaves frame."""
    frame.focus_set()
    print("Mouse has left the frame")


frame = Frame(root, width=400, height=300)
frame.bind("<Button-1>", mouse_left_clicked)
frame.bind("<Button-2>", mouse_middle_clicked)
frame.bind("<Button-3>", mouse_right_clicked)
frame.bind("<Enter>", mouse_enter)
frame.bind("<Leave>", mouse_leave)
frame.bind("<Key>", key)
frame.pack()

root.title('Tk focus, mouse, key press detect demo.')
root.eval('tk::PlaceWindow . Center')

root.mainloop()
