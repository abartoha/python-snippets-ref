"""check tk_tools installed.
   By Steve Shambles.
   stevepython.wordpress.com
   code-snippet-vol_41-snip_201

"""
import sys
from tkinter import messagebox, Tk

root = Tk()
root.withdraw()

try:
    import tk_tools # Change this to any import you want to check for.

except ImportError:
    messagebox.showwarning('Warning',
                           'tk_tools is not installed.\n\n'
                           'Please pip3 install tk_tools.')
    root.destroy()
    sys.exit()


print("tk_tools is installed")
