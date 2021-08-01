"""Code snippets vol-51.
   Snippet 253-Barciode creator.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements: pip3 install python-barcode

Origin:
https://pypi.org/project/python-barcode/
"""
import webbrowser as web

import barcode
from barcode.writer import ImageWriter

EAN = barcode.get_barcode_class('ean13')
ean = EAN('5000168001159', writer=ImageWriter()) #13 digits number only
fullname = ean.save('barcode')

# Point your phone camera at the barcode image to read it.
# Then click the search button and you will see this
# barcode is a packet of McVites digestive biscuitsa.
web.open('barcode.png')
