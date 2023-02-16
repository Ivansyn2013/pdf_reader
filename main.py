import PyPDF2

from colorama import Fore, Back, Style
from PIL import Image

with open('infiles/2016-catalogo-terumo.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    print(f'Number of Pages in PDF File is {len(pdf_reader.pages)}')
    print(f'PDF Metadata is {pdf_reader.metadata}')
    print(pdf_reader.get_fields())
    print(pdf_reader)


    print(Fore.BLUE+ f'PDF File Creator is {pdf_reader.metadata["/Creator"]}')
    print(Fore.RESET+ Style.DIM+'dfa')


    some_text = pdf_reader.pages[3].extract_text()


    page0 = pdf_reader.pages[0]
    # print(page0.keys())
    # print(page0['/Resources'].keys())
    # print(page0['/Resources']['/XObject'].keys())
    # i = 0
    #
    # for page in pdf_reader.pages:
    #     i += 1
    #     if '/XObject' in page['/Resources']:
    #         xObject = page['/Resources']['/XObject'].get_object()
    #         print(xObject.keys())
    #         for obj in xObject:
    #             if xObject[obj]['/Subtype'] == '/Image':
    #                 size = (xObject[obj]['/Width'],
    #                         xObject[obj]['/Height'])
    #                 data = xObject[obj].get_data()
    #                 if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
    #                     mode = "RGB"
    #                 else:
    #                     mode = "P"
    #                 if '/Filter' in xObject[obj]:
    #                     if xObject[obj]['/Filter'] == '/FlateDecode':
    #                         img = Image.frombytes(mode, size, data)
    #                         img.save(f'outfiles/{obj[1:]}_{i}'
    #                                  + ".png")
    #                     elif xObject[obj][f'/Filter'] == '/DCTDecode':
    #                         img = open(f'outfiles/{obj[1:]}_{i}' + ".jpg", "wb")
    #                         img.write(data)
    #                         img.close()
    #                     elif xObject[obj]['/Filter'] == '/JPXDecode':
    #                         img = open(f'outfiles/{obj[1:]}_{i}' + ".jp2", "wb")
    #                         img.write(data)
    #                         img.close()
    #                     elif xObject[obj]['/Filter'] == '/CCITTFaxDecode':
    #                         img = open(f'outfiles/{obj[1:]}_{i}' + ".tiff", "wb")
    #                         img.write(data)
    #                         img.close()
    #                 else:
    #                     img = Image.frombytes(mode, size, data)
    #                     img.save(f'outfiles/{obj[1:]}_{i}' + ".png")
    #     else:
    #         print("No image found.")
