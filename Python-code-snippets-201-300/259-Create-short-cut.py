"""Code snippets vol-52
   259-Create a short-cut.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg

   Blog: stevepython.wordpress.com

Windows only.
This will create a shortcut link to an exe file
and place it in the startup folder using a supplied icon.

requirements:
pip install pywin32
https://pypi.org/project/pywin32/

Origin:
#https://stackoverflow.com/questions/26986470/create-shortcut-files-in-windows-7-using-python
"""
import os
import win32com.client

# Store current directory
curr_path = os.getcwd()

# location where you want the short-cut placed.
# This is an example for Windows 7 startup folder
# so program will run at boot.
startup = r'C:/Users/All Users/Microsoft/Windows/Start Menu/Programs/Startup/'

# Name of your short-cut. eg. xxx.lnk
shrt_ct_path = os.path.join(startup, 'test.lnk')

# the exe file that the short-cut points to (in current dir).
exe_path = os.path.join(str(curr_path), 'test.exe')

# Optional name of an icon to use for the short-cut lnk. current dir
icon_path = os.path.join(str(curr_path), 'python.ico')

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(shrt_ct_path)
shortcut.Targetpath = exe_path
shortcut.IconLocation = icon_path
shortcut.WindowStyle = 1 # 7 - Minimized, 3 - Maximized, 1 - Normal
shortcut.save()
