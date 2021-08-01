'''
134-Tkinter status bar
stevepython.wordpress.com

source: Unknown and shambleized.
'''

from tkinter import Tk, Label, SUNKEN, W, BOTTOM, X

ROOT = Tk()
ROOT.title('134-Tkinter status bar')
ROOT.geometry('300x150')


status = Label(ROOT, text="Status: Ready", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

ROOT.mainloop()
