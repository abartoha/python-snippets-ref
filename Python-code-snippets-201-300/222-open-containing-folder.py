"""Code snippets vol-45-snippet-222
Open current working directory using systems filebrowser

By Steve Shambles
March 2020
stevepython.wordpress.com

Download all snippets so far:
https://wp.me/Pa5TU8-1yg
"""
import os
import webbrowser

cwd = os.getcwd()
webbrowser.open(cwd)
