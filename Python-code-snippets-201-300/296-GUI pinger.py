"""Code snippets vol-60
   296-GUI Pinger

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
None

origin:
https://www.reddit.com/r/learnpython/comments/ho8joh/question_about_tkinter/
"""
from tkinter import END, LabelFrame, Tk
from tkinter.scrolledtext import ScrolledText
import time


def ping_adress(target, myadress):
    pingms = 43
    current_time = time.strftime("%H:%M:%S")
    result = f"{current_time} = {pingms} ms"
    target.insert(END, result+'\n')
    target.see(END)  # Scroll to the bottom.


def run():
    ping_adress(label1, adress1)
    ping_adress(label2, adress2)
    root.after(1000, run)  # Run this function again in 1,000 ms.


root = Tk()
root.title("Pinger")
root.geometry("400x400")

adress1 = '8.8.8.8'
frame1 = LabelFrame(root, text=adress1)
frame1.grid(row=0, column=0, sticky='nsew')
label1 = ScrolledText(frame1)
label1.pack()

adress2 = '85.114.146.71'
frame2 = LabelFrame(root, text=adress2)
frame2.grid(row=0, column=1, sticky='nsew')
label2 = ScrolledText(frame2)
label2.pack()

# This code sets the labelframes to expand to the size of the window.
root.columnconfigure((0, 1), weight=1)
root.rowconfigure(0, weight=1)

run()  # Start loop.

root.mainloop()
