'''
Colour Sliders
from the book Adventures In Python
'''

import tkinter as tk
from tkinter import ttk, Canvas, Entry, END
window = tk.Tk()

def sliderupdate(source):
    red = redslider.get()
    green = greenslider.get()
    blue = blueslider.get()

    colour = "#%02x%02x%02x" % (red, green, blue)
    Canvas.config (bg=colour)
    hextext.delete(0, tk.END)
    hextext.insert(0, colour)

redslider = tk.Scale(window, from_=0, to=255, command=sliderupdate)
greenslider = tk.Scale(window, from_=0, to=255, command=sliderupdate)
blueslider = tk.Scale(window, from_=0, to=255, command=sliderupdate)

Canvas = tk.Canvas(window, width=200, height=200)

hextext = tk.Entry(window)

redslider.grid(row=1, column=1)
greenslider.grid(row=1, column=2)
blueslider.grid(row=1, column=3)
Canvas.grid(row=2, column=1, columnspan=3)
hextext.grid(row=3, column=1, columnspan=3)

window.mainloop
