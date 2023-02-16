import PyPDF2

from colorama import Fore, Back, Style
from PIL import Image

reader = PyPDF2.PdfReader('infiles/2016-catalogo-terumo.pdf')
writer = PyPDF2.PdfWriter

writer.add_blank_page()
writer.add_outline_item(title='Привет',
                        page_number=0,
                        color=(205, 92, 92))

with open("meta-pdf.pdf", "wb") as f:
    writer.write(f)