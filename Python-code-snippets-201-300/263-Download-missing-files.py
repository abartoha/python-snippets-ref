"""Code snippets vol-53
   263-Download missing files for your app.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg

   Blog: stevepython.wordpress.com

Requirements: pip3 install wget

Origin: Steve Shambles
https://github.com/steveshambles/Sync-It
"""
import os
from tkinter import messagebox, Tk

import wget

root = Tk()
root.withdraw()

def dwnld_yn_msgbox():
    """Offer user option to auto download missing files."""
    global ask_dl

    ask_dl = messagebox.askyesno('Question:',
                                 'Auto download missing files?\n\n'
                                 'One or more icon files are missing\n'
                                 'from the current directory.\n\n'
                                 'Should I try to download\n'
                                 'these files for you?')

def check_icons():
    """Check if icons required are present in cwd,
       if not offer to auto download them from GitHub."""
    if not os.path.exists('sync-it.ico') or not os.path.exists('sync-it-red.ico'):
        dwnld_yn_msgbox()

    if not os.path.exists('sync-it.ico'):
        if ask_dl:
            wget.download('https://raw.githubusercontent.com/steveshambles/' \
                          'Sync-It/master/sync-it.ico')

    if not os.path.exists('sync-it-red.ico'):
        if ask_dl:
            wget.download('https://raw.githubusercontent.com/steveshambles/' \
                          'Sync-It/master/sync-it-red.ico')

check_icons()
