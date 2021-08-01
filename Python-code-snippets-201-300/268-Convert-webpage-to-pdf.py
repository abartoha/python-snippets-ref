"""Code snippets vol-54
    268-Convert Webpage to PDF

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
pip install pdfkit
https://pypi.org/project/pdfkit/

download and install binary:
https://wkhtmltopdf.org/downloads.html

copy wkhtmltopdf.exe to current dir.

Origin: ?
"""
import webbrowser as web
import pdfkit

pdfkit.from_url('https://github.com/steveshambles?tab=repositories', 'out3.pdf')

web.open('out3.pdf')
