"""Code snippets vol-48-snippet-236
   PDF to images

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

requirements:
pip install PyMuPDF
https://pypi.org/project/PyMuPDF/

origin:
https://www.tutorialexample.com/best-practice-to-python-convert-pdf-to-images-for-beginners-python-tutorial/
"""
import webbrowser as wb
import fitz

PDF = 'test.pdf'
DOC = fitz.open(PDF)

for page in DOC:                          # iterate through the pages
    pix = page.getPixmap(alpha=False)     # render page to an image
    pix.writePNG('page-%i.png' % page.number)

wb.open('page-0.png')
