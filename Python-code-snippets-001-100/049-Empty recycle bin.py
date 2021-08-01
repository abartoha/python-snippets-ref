'''
49-Empty Windows Recycle Bin
 
You may need to "Pip install winshell"
 
Steve Shambles Jan 2019
 
https://stevepython.wordpress.com/
'''
 
import winshell
 
# The try-except block captures the error produced
# if the recycle bin is found to be already empty.
 
# You can change the boolean False and True statements
# to either turn on or off the following:
# Confirm yes\no dialog, progress bar, sound effect.
 
try:
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
    print("Recycle bin emptied")
 
except:
    print("Recycle bin already empty")
