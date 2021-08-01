"""Code snippets vol-55
   271-run python script from right click menu

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements: Windows only. pip3 install winregistry

Origin:
https://github.com/seddie95/python_script_in_right_click_menu/
blob/master/make_key.py
-------------------------------------------------------------
Intsructions:

Before running this script open your terminal or IDE in administrator
mode to allow for the editing of registry information.

The winreg module is required to access the contents of the
windows registry

pip install winregistry

Modify script to insert your own python script to be shown in
the context menu


warning: I don't know how to undo this once the menu is set,
delete the key probably though not tried yet.
"""
import os
import sys
import winreg as reg

# Get path of current working directory and python.exe.
cwd = os.getcwd()
python_exe = sys.executable

# optional hide python terminal in windows.
hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"

# Set the path of the context menu (right-click menu).
key_path = r'Directory\\Background\\shell\\dirlist\\'
# Change 'dirlist' to the name of your project.

# Create outer key.
key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, '&dirlister')
# Change 'dirlister' to the function of your script.

# create inner key.
key1 = reg.CreateKey(key, r"command")
reg.SetValue(key1, '', reg.REG_SZ, python_exe + f' "{cwd}\\dirlisterV0.7.py"')
# change 'dirlistrev07.py' to the name of your script.
