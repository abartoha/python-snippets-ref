"""Code snippets vol-46-snippet-228
   Set Windows Desktop image.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

source:
based on http://dzone.com/snippets/set-windows-desktop-wallpaper

Requirements:pip3 install pywin32

Image:
https://pixabay.com/photos/model-woman-conceptual-fashion-2614569/
"""
import win32api
import win32con
import win32gui

def setWallpaper(path):
    """Set the image to desktop backgrund."""
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                'Control Panel\\Desktop', 0,
                                win32con.KEY_SET_VALUE)

    # 0 = normal, 2 = stretch
    win32api.RegSetValueEx(key, 'WallpaperStyle', 0, win32con.REG_SZ, '2')

    #0 = normal, 1 = tile
    win32api.RegSetValueEx(key, 'TileWallpaper', 0, win32con.REG_SZ, '0')
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)


path = 'model.jpg'
setWallpaper(path)
