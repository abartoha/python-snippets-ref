'''
Python Code Snippets #21

104-Scrolled text reader

Tested on Python V3.6x on Windows 7 and Linux Mint 19.1.
By Steve Shambles.
'''
from tkinter import Tk, Frame, INSERT, scrolledtext

ROOT = Tk()
ROOT.title('ViewText')

FRAME0 = Frame(ROOT)
FRAME0.grid(padx=10, pady=10)

# Change bg to any colour you want for the background
# fg for ink colour of text.

# Change width and height for different sizes, in characters.
TXT = scrolledtext.ScrolledText(FRAME0, bg='gold', fg='black',  \
                                width=70, height=30)
TXT.grid()

# The text file to be read in and displayed.
with open("test.txt", "r") as f:
    text_contents=f.read()

TXT.insert(INSERT, text_contents)

ROOT.mainloop()
