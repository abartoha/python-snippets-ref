""""Code snippets vol-49-snippet-245
    Resize image keeping aspect ration.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements:pip3 install Pillow

Origin:
https://gist.github.com/tomvon/ae288482869b495201a0
"""
import PIL
from PIL import Image

# Your image to resize
img = Image.open('crowd.jpg')

# Set mywidth to the desired with in pixels.
mywidth = 160

wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)

# Choose your save name for resized image.
img.save('crowd-160.jpg')
