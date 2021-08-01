"""Code snippets vol-59
   292-Unshorten a URL

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
pip3 install unshortenit

https://stackoverflow.com/questions/4201062/how-can-i-unshorten-a-url
"""
from unshortenit import UnshortenIt

unsh = UnshortenIt()
uri = unsh.unshorten('https://wp.me/Pa5TU8-2yD')
print(uri)
