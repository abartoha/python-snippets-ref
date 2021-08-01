'''
Python Code Snippets #22
108-Insert image on every page of a pdf

Tested on Python V3.6x, Window 7

pip3 install PyMuPDF

source:
http://code.activestate.com/recipes/580803-inserting-images-on-pdf-pages/
'''
# PyMuPDF module.
import fitz

# Open your PDF.
doc = fitz.open("test.pdf")

# Where to place image: use upper left corner
rect = fitz.Rect(0, 0, 100, 100)

for page in doc:
    page.insertImage(rect, filename = "test.jpg") # Image to insert.

# Do an incremental save.
doc.saveIncr()
