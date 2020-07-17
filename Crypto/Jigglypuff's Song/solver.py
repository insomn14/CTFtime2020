from PIL import Image
from numpy import *

filename = 'solved1.bmp'

F_img = Image.open(filename)
img = array(F_img)

print([i for i in img[0]])

# a, b, c = img.shape
# #print(img.shape)

# for x in range(0, a):
#     for y in range(0, b):
#         pixel = img[x, y]
#         if pixel.any():
#             for i in range(0,3):
#                 pixel[i] = 000
#             img[x][y] = pixel

# get = Image.fromarray(img)
# get.save('Modif_'+filename)
