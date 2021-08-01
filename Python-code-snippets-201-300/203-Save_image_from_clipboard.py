"""Save image from clipboard
   stevepython.wordpress.com
   code-snippet-vol_41-snip_203
   By Steve Shambles.

required:
pip3 install pillow
"""
import os
import sys
import webbrowser

from PIL import ImageGrab

# Grab image from clipboard if there is one.
img = ImageGrab.grabclipboard()
file_name = 'clipboard.png'

if img:
  img.save(file_name, 'PNG')
  print('Clipboard image found and saved as', file_name)
  webbrowser.open(file_name)

else:
  print('No image data found on clipboard')


