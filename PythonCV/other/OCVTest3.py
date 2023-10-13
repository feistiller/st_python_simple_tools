import cv2


def clmap(v, k, upBound):  # mul and clamp
    val = v * k
    if val > upBound:
        return upBound
    else:
        return val


inImage_1 = 'bTest.jpg'  #
inImage_2 = 'gTest.jpg'  #

dif_img = 'dif_' + inImage_1

img_1 = cv2.imread(inImage_1)  # read as color image
img_2 = cv2.imread(inImage_2)

dif = img_1.copy()
show_dif = dif.copy()  # dif image for show only

width = img_1.shape[0]  # get width
height = img_1.shape[1]  # get height

for i in range(width):
    for j in range(height):
        # dif[i, j] = [128,0,0]      # b g r
        # print img_1[i,j]-img_2[i,j]

        diff = int(img_1[i, j][0]) - int(img_2[i, j][0])

        if diff < 0:
            show_dif[i, j] = [0, clmap(abs(diff), 10, 255), 0]

        elif diff > 0:
            show_dif[i, j] = [0, 0, clmap(abs(diff), 10, 255)]
        else:
            show_dif[i, j] = [0]

        dif[i, j] = [abs(diff)] * 3

print dif_img
print 'different data:'
print 'max : ', dif.max()
print 'min : ', dif.min()
print 'mean : ', dif.mean()

cv2.imwrite(dif_img, show_dif)

cv2.imshow('_dif', show_dif)
cv2.waitKey(0)
cv2.destroyAllWindows()