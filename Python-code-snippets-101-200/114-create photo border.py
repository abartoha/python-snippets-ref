'''
create photo border
https://snipplr.com/view/56634/create-photo-frame/
'''

import os, sys, webbrowser
from PIL import Image, ImageOps

WHITE_BORDER = 5
BLACK_BORDER = 5

img = Image.open("test.jpg")

img = ImageOps.expand(img,border = BLACK_BORDER, fill = 'red')
img = ImageOps.expand(img,border = WHITE_BORDER, fill = 'white')
img = ImageOps.expand(img,border = BLACK_BORDER, fill = 'blue')

img.save("border.jpg")
webbrowser.open("border.jpg")


