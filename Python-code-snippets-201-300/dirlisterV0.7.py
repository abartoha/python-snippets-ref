"""
Directory lister and saver V0.8
Steve Shambles Sept 2019

Saves a list of all files found in the selected directory,
but not sub-dirs, into a text file.

stevepython.wordpress.com
"""
import os
from tkinter import Tk, filedialog
import webbrowser

root = Tk()
# Hide uneeded tk window.
root.withdraw()

# Ask user for directory s\he wants files listed.
dir_sel = filedialog.askdirectory(title='Please select a directory.')

# Set up some heading strings to print.
list_dir = ('All files found in: '+str(dir_sel))
under_line = ('-' *40)


# Write header strings to text file.
with open('listing.txt', 'w') as f:
    f.write(list_dir)
    f.write('\n')
    f.write(under_line)
    f.write('\n')

    # Walk through the files in the selected directory.
    for sham, dirs, files in os.walk(dir_sel, topdown=True):
        dirs.clear() #with topdown true, this will prevent walk from going into subs dirs.

        for file in files:
            f.write(file) # write each file to text listing.
            f.write('\n') # New line.

# Open the list of files in default text viewer.
webbrowser.open('listing.txt')

# Open the listed directory in default file viewer.
webbrowser.open(dir_sel)
