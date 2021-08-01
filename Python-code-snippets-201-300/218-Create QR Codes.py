"""Code snippets vol-44-snip-218
218-Create QR Codes

requires:
pip install pyqrcode

original source:
https://www.geeksforgeeks.org/python-generate-qr-code-using-pyqrcode-module/
"""
import webbrowser
import pyqrcode
#from pyqrcode import QRCode
# String to encode. You can use a lot of links or lots of text if you want.
qr_str = 'stevepython.wordpress.com'

# Generate QR code.
gen_code = pyqrcode.create(qr_str)

# Create and save the qr image.
# You may want to expiremnt with the scale variable
# to get your desired qrimage size.
gen_code.svg('my_qr.svg', scale=8)

# Display the image in default app or web browser.
webbrowser.open('my_qr.svg')

"""
The related Qr code article to this code, Feb 2020.
https://stevepython.wordpress.com/2020/02/27/how-to-create-qr-codes
---
Download 240+ no nonsense python code snippets:
https://wp.me/Pa5TU8-1yg
"""
