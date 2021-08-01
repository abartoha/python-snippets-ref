'''
Python Code Snippets - stevepython.wordpress.com

148-Get the differnce of two images in a new image

https://stackoverflow.com/questions/189943/
how-can-i-quantify-difference-between-two-images/196882#196882
'''

import webbrowser
from PIL import Image
from PIL import ImageChops


im1 = Image.open("henry-orig.jpg")
im2 = Image.open("henry-notext.jpg")
#im2 = Image.open("henry-diff2.jpg")


diff = ImageChops.difference(im2, im1)

diff.save("diff.png")
webbrowser.open("diff.png")
