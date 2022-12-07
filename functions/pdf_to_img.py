from pdf2image import convert_from_path

# from pdfminer.high_level import extract_text

# text = extract_text(myfile)

# print(text)

# convert pdf to images PNG
def convertToImg(pdfPath,save_dir, res = 200):
    print('Loading...')
    pages = convert_from_path(pdfPath,res)


    #loop over all the pages
    for idx,page in enumerate(pages):
        page.save(f'{save_dir}/{idx}.png','PNG')
        print(f'page {idx} done')
    print('success')



# convertToImg(myfile,'/home/hamada/Documents/Projects/DarkPdf/Elite/')
