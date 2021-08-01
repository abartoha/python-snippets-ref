"""
Python code snippets vol 37:
184-Folder of images to pdf
stevepython.wordpress.com

requirements:
pip3 install fpdf
pip3 install pillow

source:
https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images
"""
import os
from fpdf import FPDF
from PIL import Image


listPages = os.listdir("images")

def makePdf(pdfFileName, listPages, dir=''):
    if dir:
        dir += "/"

    cover = Image.open(dir + str(listPages[0]))
    width, height = cover.size

    pdf = FPDF(unit="pt", format=[width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page), 0, 0)

    pdf.output(pdfFileName + ".pdf", "F")

makePdf('output.pdf', listPages, 'images')
