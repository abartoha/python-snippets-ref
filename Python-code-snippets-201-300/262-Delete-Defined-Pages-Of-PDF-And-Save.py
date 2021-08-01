"""Code snippets vol-53
   262-Delete-Defined-Pages-Of-PDF-And-Save

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg

   Blog: stevepython.wordpress.com

Requirements:
pip3 install pikepdf
https://pypi.org/project/pikepdf/

Origin:
https://pikepdf.readthedocs.io/en/latest/tutorial.html
https://github.com/pikepdf/pikepdf
"""
from pikepdf import Pdf

# Open a pdf file.
pdf = Pdf.open('my.pdf')

# How many pages are there?
print(len(pdf.pages))

# Remove pages 2-3
del pdf.pages[1:3]

# How many pages now?
print(len(pdf.pages))

# Save new PDF.
pdf.save('new.pdf')
