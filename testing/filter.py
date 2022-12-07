from PIL import Image, ImageOps
import os
from pytesseract import pytesseract
# secound try with invertion (much faster)
# def darkmode(img,name,save_dir):
#     pixels = []
#     counter =0
#     for x in range(100):
#         for y in range(100):
#             pix = img.getpixel((x,y))
#             pixels.append(pix)
#     for i in pixels:
#         if i ==(255,255,255):
#             counter += 1
    
#     if counter == len(pixels):
#         inv = ImageOps.invert(img)
#         inv.save(f'{save_dir}/D{name}')
#         print(f'page{name} text done')
#     else:
#         img.save(f'{save_dir}/D{name}')
#         print(f'page{name} colored done')

# def PhotoSearch(input_dir,out_dir):
#     for file in os.listdir(input_dir):
#         img = Image.open(os.path.join(input_dir,file))
#         darkmode(img,file,out_dir)
#     print('Done')

# inpu = input('Name the folder that has White energy: ')
# outpu = input('Name the folder to save pixs in: ')


# first try with pixels(slow af)
# w = img.width
# h = img.height
# def darkmode(img):
#     print('Loading...')
#     for x in range(w):
#         for y in range(h):
#             # turn any white color to black
#             if img.getpixel((x,y)) == (255, 255, 255):
#                 img.putpixel((x,y),(0,0,0))

#                 # turn anycolor (from black to grey) to white
#             elif img.getpixel((x,y)) <= (0,0,0) :
#                 img.putpixel((x,y),(255,255,255))
#     img.save('/home/hamada/Documents/Projects/DarkPdf/testing/D2.png')
#     print('done')

# darkmode(img)


# third try (i am a fucken genius) if there is text more than 20 words on a page then apply the filter
# takes longer than 2nd try tho but look at the results

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

img = Image.open('/home/hamada/Documents/Projects/DarkPdf/testing/imgs/0.png')

# # darkmode(img,'16.png','/home/hamada/Documents/Projects/DarkPdf/testing/Dimgs/')


# PhotoLoop('/home/hamada/Documents/Projects/DarkPdf/testing/imgs/',
#           '/home/hamada/Documents/Projects/DarkPdf/testing/Dimgs/')


# i want to try and invert a spicific apace in an img
# 4th pixels(slow af)
w = img.width
h = img.height
hh = round(img.height/1.5)


def darkmode(img):
    print('Loading...')
    for x in range(w):
        for y in range(0,hh):
            # turn any white color to black
            R = img.getpixel((x,y))[0]
            G = img.getpixel((x,y))[1]
            B = img.getpixel((x,y))[2]
            img.putpixel((x,y),(255-R,255-G,255-B))


    img.save('/home/hamada/Documents/Projects/DarkPdf/testing/D4.png')
    print('done')

darkmode(img)
