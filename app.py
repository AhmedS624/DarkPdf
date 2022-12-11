import os
import time
import shutil
import subprocess
from functions.filter import PhotoLoop
from functions.imgs_to_pdf import img2pdf
from functions.pdf_to_img import convertToImg


parent_dir = '/home/hamada/Documents/Projects/DarkPdf'
pdf = input('Name of the pdf file in pdf folder : ')
Dpdf = pdf.split('.')[0]
W_imgs = 'White_folder'
D_imgs = 'Dark_imgs'


    
pdf_path = f'{parent_dir}/pdf/{pdf}'
# err pre check if folder exists
try:
    os.mkdir(f'{parent_dir}/{W_imgs}')
    os.mkdir(f'{parent_dir}/{D_imgs}')
except:
    print('file Error')
W_imgs_path = os.path.join(parent_dir,W_imgs)
D_imgs_path = os.path.join(parent_dir,D_imgs)

print('Folders Created')
time.sleep(1)
print('initiate Pdf to imgs')

convertToImg(pdf_path,W_imgs_path)

time.sleep(1)
print('initiate filtering')

PhotoLoop(W_imgs_path,D_imgs_path)

time.sleep(1)
print('initiate Dark imgs to pdf')

time.sleep(1)
img2pdf(D_imgs_path,f'pdf/{Dpdf}.pdf')

time.sleep(1)

print('Deleting useless folders')
shutil.rmtree(f"{parent_dir}/{W_imgs}")
shutil.rmtree(f"{parent_dir}/{D_imgs}")

print('Success')
time.sleep(1)
print('opening file')
time.sleep(1)

subprocess.call(['xdg-open',f"pdf/{Dpdf}.pdf"])
