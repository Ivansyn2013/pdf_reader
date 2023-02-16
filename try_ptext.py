from pathlib import Path

from borb.pdf import  Document
from borb.pdf import  Page
from borb.pdf import  SingleColumnLayout
from borb.pdf import  Paragraph
from borb.pdf import  PDF
from borb.pdf import  HexColor
from borb.pdf import PageLayout
from borb.pdf import Image

from decimal import Decimal

FONTS = [
        "Courier",
        "Courier-Bold",
        "Courier-Bold-Oblique",
        "Courier-Oblique",
        "Helvetica",
        "Helvetica-Bold",
        "Helvetica-Bold-Oblique",
        "Helvetica-Oblique",
        "Symbol",
        "Times-Bold",
        "Times-Bold-Italic",
        "Times-Italic",
        "Times-Roman",
        "ZapfDingbats",
    ]


pdf = Document()
page = Page()
pdf.add_page(page)

#layout.add(Paragraph('Hellow World!!', font_size=20, font_color=HexColor('#FA8072')))

layout = SingleColumnLayout(page)


layout.add(Paragraph('Hellow World!!',
                     font_size=20,
                     font_color=HexColor('FA8072'),
                     ))
layout.add(Image(Path('outfiles/Im0_5.jpg')))

with open(Path('outfiles/out.pdf'),'wb') as pdf_file:
    PDF.dumps(pdf_file, pdf)

#https://github.com/jorisschellekens/borb-examples#223-setting-a-pagelayout