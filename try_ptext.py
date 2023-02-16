from pathlib import Path

from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf import HexColor
from borb.pdf import PageLayout
from borb.pdf import Image
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont
from decimal import Decimal

from text import TEXT

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

font_path = Path('ofont.ru_Zekton.ttf')
custom_font = TrueTypeFont.true_type_font_from_file(font_path)
pdf = Document()
page = Page()
pdf.add_page(page)

# layout.add(Paragraph('Hellow World!!', font_size=20, font_color=HexColor('#FA8072')))

layout = SingleColumnLayout(page)
layout.add(Image(Path('infiles/logo.png'), width=Decimal(150), height=Decimal(50)))

layout.add(Paragraph('Описание', font_size=20,
                     font=custom_font))
layout.add(Image(Path('outfiles/Im0_5.jpg')))
layout.add(Paragraph('Описание',
                     font_size=14,
                     font=custom_font
                     ))

layout.add(Paragraph(TEXT,
                     font_size=10,
                     font=custom_font
                     ))

with open(Path('outfiles/out.pdf'), 'wb') as pdf_file:
    PDF.dumps(pdf_file, pdf)

# https://github.com/jorisschellekens/borb-examples#223-setting-a-pagelayout
