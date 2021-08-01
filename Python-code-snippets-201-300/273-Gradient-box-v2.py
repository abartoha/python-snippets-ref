"""Code snippets vol-55
   273-Gradient box v2

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
pip3 install numpy
pip3 install Pillow

Origin:
Thanks to Finn McCool for sendig in this snippet.
https://thatsenoughofthat.com/
https://wordpress.com/comment/stevepython.wordpress.com/1390
"""
import numpy as np
from PIL import Image

img_array = np.ones([255, 255, 3], dtype=np.uint8) * 255

for i in range(0, 256):
    img_array[i:, :, 1:2] = i

my_image = Image.fromarray(img_array)
my_image.save('gradient.png')
my_image.show()  # Did not display on Linux Mint, but saved ok.
