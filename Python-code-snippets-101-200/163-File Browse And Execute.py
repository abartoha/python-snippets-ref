"""
Python code snippets vol 33:
163-File browser and executor
stevepython.wordpress.com

Source:
Steve Shambles Oct 2019
Knocked this up to save time when I need a file selector
in my Tkinter GUI.

Added the execute file bit to make it a bit more interesting.
"""
from tkinter import filedialog, Tk, Button, Entry, LabelFrame
import webbrowser

root = Tk()
root.title('File selector')

def get_file():
    """Get file from user and execute its linked app"""
    users_file = filedialog.askopenfilename(title='Please Select a file')
    entry1.delete(0, 'end')
    entry1.insert(0, users_file)
    webbrowser.open(users_file)

frame1 = LabelFrame(root, text='Click browse to choose a file')
frame1.grid(padx=20, pady=10)

entry1 = Entry(frame1)
entry1.grid(padx=5, pady=5)

btn1 = Button(frame1, text='Browse', command=get_file)
btn1.grid(row=0, column=1, padx=8, pady=15)

root.mainloop
