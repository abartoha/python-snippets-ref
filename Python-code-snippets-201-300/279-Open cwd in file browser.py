"""Code snippets vol-56
   279-Open cwd in file browser.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
None

Origin:
Steve Shambles.
"""
import os
import webbrowser

cwd = os.getcwd()
webbrowser.open(cwd)
