import bHash as b
from PIL import Image

Image_1 = "C:/Users/admin/Desktop/6.jpg"  #
Image_2 = 'F:/Python/PythonOpenCV2016052402/Test/5.jpg'  #

for i in range(1, 5):
    img_1 = Image.open(Image_1)  # read as color image
    img_2 = Image.open(Image_2)
    num = b.classfiy_dHash(img_1,img_2)
    print(num)