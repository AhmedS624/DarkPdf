from PIL import Image, ImageOps
import os
from pytesseract import pytesseract

# secound try with invertion (much faster)
# uncomment when want to use

def darkmode(img,name,save_dir):
    pixels = []
    counter =0
    for x in range(100):
        for y in range(100):
            pix = img.getpixel((x,y))
            pixels.append(pix)
    for i in pixels:
        if i ==(255,255,255):
            counter += 1
    
    if counter == len(pixels):
        inv = ImageOps.invert(img)
        inv.save(f'{save_dir}/D{name}')
        print(f'page{name} text done')
    else:
        img.save(f'{save_dir}/D{name}')
        print(f'page{name} colored done')

def PhotoLoop(input_dir,out_dir):
    for file in os.listdir(input_dir):
        img = Image.open(os.path.join(input_dir,file))
        darkmode(img,file,out_dir)
    print('Done')

# inpu = input('Name the folder that has White energy: ')
# outpu = input('Name the folder to save pixs in: ')



# third try (i am a fucken genius) if there is text more than 20 words on a page then apply the filter
# takes longer than 2nd try tho but look at the results
# un comment when you want to use it

# def darkmode(img,name,save_dir):
#     words = []
#     text = pytesseract.image_to_string(img)
#     words = text.split(' ')
        
#     if len(words) > 150:
#         inv = ImageOps.invert(img)
#         inv.save(f'{save_dir}/D{name}')
#         print(f'page{name} text done')
#     else:
#         img.save(f'{save_dir}/D{name}')
#         print(f'page{name} colored done')

# def PhotoLoop(input_dir,out_dir):
#     for file in os.listdir(input_dir):
#         img = Image.open(os.path.join(input_dir,file))
#         darkmode(img,file,out_dir)
#     print('Done')
