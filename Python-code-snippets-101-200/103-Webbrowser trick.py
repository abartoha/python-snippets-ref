'''
Python Code Snippets #21

103-Webbrowser trick

Tested on Python V3.6 on Windows 7 and Linux Mint 19.1.

'''

import webbrowser
# Webbrowser can open any file type, as long as it has a
# app associated with it on the current system.

# Examples. Assuming the test files are in current working directory.
webbrowser.open("test.txt")
webbrowser.open("test.mp3")
webbrowser.open("test.exe")
webbrowser.open("test.pdf")
