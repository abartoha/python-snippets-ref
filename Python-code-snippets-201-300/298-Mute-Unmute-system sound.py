"""Code snippets vol-60
   298-Mute-unmute-sound on Windows

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
Windows 7,8,10

origin:
# I Stripped out from code here:
# https://github.com/Paradoxis/Windows-Sound-Manager

# run this to mute sound, run again to unmute
# windows only 7,8,10

#more keys:
# Keyboard.key(Keyboard.VK_VOLUME_UP)
# Keyboard.key(Keyboard.VK_VOLUME_DOWN)

# All keys here:
# https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
"""
from keyboard import Keyboard


def mute_sound():
    """Press audio mute key on keyboard, call again to toggle."""
    Keyboard.key(Keyboard.VK_VOLUME_MUTE)


mute_sound()
