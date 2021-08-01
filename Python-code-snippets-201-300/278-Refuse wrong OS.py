"""Code snippets vol-56
   278-Refuse wrong OS.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
None

Origin:
Steve Shambles.
"""
import sys
from tkinter import messagebox, Tk

root = Tk()
root.withdraw()

if sys.platform != 'linux':
    # Change 'linux' to 'win32' or 'posix' if required.
    messagebox.showerror('OS Error!',
                         'This code cannot run on this operating system.')

    sys.exit()
