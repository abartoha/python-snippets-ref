"""Code snippets vol-46-snippet-229
   Get screen resolution
   Windows only.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements:pip3 install pywin32

Source:
http://timgolden.me.uk/python/win32_how_do_i/find-the-screen-resolution.html
"""
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

print("Screen resolution = %dx%d" % (width, height))
