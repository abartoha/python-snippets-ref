'''
Python Code Snippets #21

105-Tkinter menu tick

Tested on Python V3.6x on Windows 7 and Linux Mint 19.1.
By Steve Shambles

'''
from tkinter import Tk, Menu, Checkbutton, IntVar, Frame

ROOT = Tk()
ROOT.title('Menu check mark example')

def use_clean_insults():
    cleanVar.set(1)
    rudeVar.set(0)

def use_rude_insults():
    cleanVar.set(0)
    rudeVar.set(1)

# set vars up menu check
cleanVar=IntVar()
cleanVar.set(1)#start off as default menu option
rudeVar=IntVar()
rudeVar.set(0)

MENU_BAR = Menu(ROOT)
INSULTS_MENU = Menu(MENU_BAR, tearoff=0)
MENU_BAR.add_cascade(label="Insults", menu=INSULTS_MENU)
INSULTS_MENU.add_checkbutton(label="Use Clean Insults", variable=cleanVar, command=use_clean_insults)
INSULTS_MENU.add_checkbutton(label="Use Rude Insults", variable=rudeVar, command=use_rude_insults)
ROOT.config(menu=MENU_BAR)


ROOT.mainloop()
