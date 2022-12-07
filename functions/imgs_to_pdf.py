import os
from PIL import Image
import re


def img2pdf(input_dir,output_dir):
        image_list = []
        image_ext = ('jpeg','png','jpg')
        filename = []
        print('Loading...')
        #put all images in list
        for file in os.listdir(input_dir):
                if file.rsplit('.')[-1] in image_ext:
                        filename.append(file)
        #sort the list 0 => highest page number

        # print(filename) # testing
        p = re.compile(r'\d+')
        filename = sorted(filename, key=lambda s: int(p.search(s).group()))
        # print(filename) # testing

        # open every image then invert it
        for i in filename:
                img = Image.open(os.path.join(input_dir,i))
                img = img.convert('RGB')
                image_list.append(img)
        # save as pdf
        image_list[0].save(output_dir,save_all=True,append_images=image_list[1:])
        print('Done')

# folder = input('Name of the folder that has the images: ')
# input = f'/home/hamada/Documents/Projects/DarkPdf/{folder}'
# output = f'pdf/{folder}.pdf'

# img2pdf(input,output)
