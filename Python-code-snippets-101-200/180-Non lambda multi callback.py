"""
Python code snippets vol 36:
180-Non lambda multi callback
stevepython.wordpress.com

source:
https://stackoverflow.com/questions/16074486/python-tkinter-button-callback/16074917#16074917
"""
import tkinter as tk

root = tk.Tk()
root.geometry('405x50')

def myfunction(event):
    """Button callback"""
    print(buttons[event.widget])

buttons = {}
for i in range(7):
    b = tk.Button(root, text='button' + str(i))
    buttons[b] = i # save button, index as key-value pair
    b.bind('<Button-1>', myfunction)

    b.place(y=10, x=(10+(55*i)))  # place version.
    #b.grid(column=(0+i),row=0)   # grid version.
    #b.pack(side=LEFT)            # pack version.

root.mainloop()
