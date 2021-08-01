
from glob import glob

"""
Run this in the directory where your images are and where you want
the index.html file to be.
https://snipt.net/public/tag/python/?page=13
"""

index = open("index.html", "w+")
files = glob("*.png") + glob("*.gif") + glob("*.jpg")
files.sort()

for file in files:
    #str = '<a href="%s">%s</a><br>' % (file, file)
    str = '<img src="%s">%s</a><br>' % (file, file)

    print(str, file=index)

index.close()

