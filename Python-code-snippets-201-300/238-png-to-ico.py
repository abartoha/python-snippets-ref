"""Code snippets vol-48-snippet-238
    PNG to Ico.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements: pip3 install imageio
https://imageio.readthedocs.io/en/stable/installation.html

origin:
https://stackoverflow.com/questions/45507/is-there-a-python-library-for-generating-ico-files

"""
import imageio

IMG = imageio.imread('test.png')
imageio.imwrite('test.ico', IMG)
