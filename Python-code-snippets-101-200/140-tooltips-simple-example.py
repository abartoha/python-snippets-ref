'''
140-Tooltips module simple example
stevepython.wordpress.com

source:
https://stevepython.wordpress.com/2019/08/16/how-to-create-a-cool-module
'''

from tkinter import Tk, Button
import ttips

root = Tk()

btn = Button(root, text='A Button')
btn.pack()

ttips.Create(btn, "This is a tooltip")

root.mainloop()
