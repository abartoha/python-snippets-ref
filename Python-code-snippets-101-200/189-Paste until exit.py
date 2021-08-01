"""
Python code snippets vol 38:
189-Paste until exit
stevepython.wordpress.com

requirements: pip3 install pyperclip

source:
https://gist.github.com/klevyr/60655d9d3e4aff3d127055909188238b
"""

import pyperclip as clipbd
# Capture the information from your clipboard and paste them into a
# file until the text "EXIT!" Is copied.

lastdata = ""
f = open("Product.txt", "a+")

while clipbd.paste() != 'EXIT!':
    if lastdata == clipbd.paste():
        continue

    else:
        lastdata = clipbd.paste()
        print(lastdata)
        i = 0
        for line in lastdata.split(sep="\r\n"):
            i = i + 1
            if i >= 8 and i < 22:
                f.write("{}\n".format(line.strip()))

f.close()
