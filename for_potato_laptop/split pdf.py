from PyPDF2 import PdfFileWriter, PdfFileReader
import os

def split_pdf_to_two(filename,page_number):
    counter = 1
    pdf_reader = PdfFileReader(open(filename, "rb"))
    try:
        assert page_number < pdf_reader.numPages
        pdf_writer2 = PdfFileWriter()

        while True:
            pdf_writer1 = PdfFileWriter()
            if page_number*counter > pdf_reader.getNumPages():
                break
            for page in range(page_number):
                page = page+(50*(counter-1))
                pdf_writer1.addPage(pdf_reader.getPage(page))
            with open(f"result/part{counter}.pdf", 'wb') as file1:
                pdf_writer1.write(file1)
                print(f'part {counter} done')
                counter += 1

        for page in range(page_number*(counter - 1),pdf_reader.getNumPages()):
            pdf_writer2.addPage(pdf_reader.getPage(page))

        with open(f"result/part{counter}.pdf", 'wb') as file2:
            pdf_writer2.write(file2)
        print(f'part {counter} done')
        print('Finished')


    except AssertionError:
        print('Error:page number too large')
       
        



name = input('name of thy pdf : ')
num = input('Number of pages to DIVIDE by: ')

split_pdf_to_two(name,int(num))
