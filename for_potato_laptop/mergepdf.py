from PyPDF2 import PdfFileMerger, PdfFileReader
merger = PdfFileMerger()
print('when done press enter again')

while True:
    inp = input('pdf file name: ')
    if inp == '':
        break
    file = open(f'Darkpdfs/{inp}','rb')
    merger.append(PdfFileReader(file))

merger.write("merged.pdf")

print('sucess')
