from PIL import Image
from numpy import *

filename1 = 'chal.png'
filename2 = 'goose_stole_the_key.png'

F_img1 = Image.open(filename1)
img1 = array(F_img1)
F_img2 = Image.open(filename2)
img2 = array(F_img2)


a, b, c = img1.shape
#print(img.shape)

for x in range(0, a):
    for y in range(0, b):
        pixel1 = img1[x, y]
        pixel2 = img2[x, y]
        if pixel1.any():
            for i in range(0,3):
                pixel2[i] = pixel1[i] ^ pixel2[i]
            img2[x][y] = pixel2

get = Image.fromarray(img2)
get.save('solve.png')
