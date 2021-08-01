'''
132-Tkinter PanedWindow
sources, a mixture from here and there
https://effbot.org/tkinterbook/panedwindow.htm
https://www.tutorialspoint.com/python/tk_panedwindow

and added my own slant
'''
from tkinter import Tk, PanedWindow, VERTICAL, BOTH, Label

root = Tk()
root.title('PanedWindow Example')
root.geometry('400x400')


m1 = PanedWindow(showhandle=True)
m1.pack(fill=BOTH, expand=1)

left = Label(m1, bg="skyblue", text="Left PanedWindow", relief="sunken", bd=4)
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL, showhandle=True)
m1.add(m2)

top = Label(m2, bg="red", text="Top PanedWindow", relief="sunken", bd=4)
m2.add(top)

bottom = Label(m2, bg="gold", text="Bottom PanedWindow", relief="sunken", bd=4)
m2.add(bottom)

root.mainloop()
