"""Code snippets vol-46-snippet-230
Get Windows desktop folder

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements:pip3 install pywin32

Source:
http://timgolden.me.uk/python/win32_how_do_i/get-the-desktop-folder.html
"""
from win32com.shell import shell, shellcon

print(shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0))
