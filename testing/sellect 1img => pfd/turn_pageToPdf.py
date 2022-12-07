from PyPDF2 import PdfFileWriter, PdfFileReader
import os

def turn_to_pdf(filename,page_number):
    pdf_reader = PdfFileReader(open(filename, "rb"))
    try:
        assert page_number < pdf_reader.numPages

        pdf_writer1 = PdfFileWriter()
        if page_number > pdf_reader.getNumPages():
            print('you entered the wrong page number')
            exit()
        pdf_writer1.addPage(pdf_reader.getPage(page_number-1))
        with open(f"img{page_number}.pdf", 'wb') as file1:
            pdf_writer1.write(file1)
            print(f'img{page_number} done')

        
        print('Finished')


    except AssertionError:
        print('Error:page number too large')
       
        



name = input('name of thy pdf : ')
num = input('Number of the page you want to convert to pdf: ')

turn_to_pdf(name,int(num))
