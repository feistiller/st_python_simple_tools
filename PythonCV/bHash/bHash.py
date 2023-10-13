from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps

def getCode(img, size):
    result = []
    # print("x==",size[0])
    # print("y==",size[1]-1)

    x_size = size[0] - 1  # width
    y_size = size[1]  # high
    for x in range(0, x_size):
        for y in range(0, y_size):
            now_value = img.getpixel((x, y))
            next_value = img.getpixel((x + 1, y))

            if next_value < now_value:
                result.append(1)
            else:
                result.append(0)

    return result


def compCode(code1, code2):
    num = 0
    for index in range(0, len(code1)):
        if code1[index] != code2[index]:
            num += 1
    return num


def classfiy_dHash(image1, image2, size=(9, 8)):
   
    image1 = image1.resize(size).convert('L')
    code1 = getCode(image1, size)

    image2 = image2.resize(size).convert('L')
    code2 = getCode(image2, size)

    assert len(code1) == len(code2), "error"

    return compCode(code1, code2)


__all__ = [classfiy_dHash]