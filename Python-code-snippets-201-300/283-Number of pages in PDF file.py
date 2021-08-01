"""Code snippets vol-57
   283-Number of pages in a PDF file.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
pip3 install pdfminer

Origin:
https://gist.github.com/miodeqqq/0a06c395b21cec60a7e0d8abe7a0793f
"""

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdftypes import resolve1

with open('test.pdf', 'rb') as f:
    parser = PDFParser(f)
    doc = PDFDocument(parser)
    parser.set_document(doc)
    pages = resolve1(doc.catalog['Pages'])
    pages_count = pages.get('Count', 0)
    print(pages_count, 'pages')
