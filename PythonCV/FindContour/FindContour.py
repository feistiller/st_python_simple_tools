#!/usr/bin/env python
# encoding: utf-8
import cv2
import numpy as np
import bHash as b
from PIL import Image


img = cv2.imread('C:/Users/admin/Desktop/6.jpg')
orig = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

_, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, contours, -1, (0, 0, 255), 50)
# show all Contours pic
# cv2.imshow("img", img)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None
# loop over our contours
for c in contours:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # if our approximated contour has four points,(the book is a rectangle)
    # we can assume that we have found our book
    if len(approx) == 4:
        screenCnt = approx
        break
# draw rectangle
cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 5)
#print screenCnt
#cv2.imshow("img", img)

# crop function
pts = screenCnt.reshape(4, 2)
rect = np.zeros((4, 2), dtype="float32")

# the top-left point has the smallest sum whereas the
# bottom-right has the largest sum
s = pts.sum(axis=1)
rect[0] = pts[np.argmin(s)]
rect[2] = pts[np.argmax(s)]

# compute the difference between the points -- the top-right
# will have the minumum difference and the bottom-left will
# have the maximum difference
diff = np.diff(pts, axis=1)
rect[1] = pts[np.argmin(diff)]
rect[3] = pts[np.argmax(diff)]

# multiply the rectangle by the original ratio
# now that we have our rectangle of points, let's compute
# the width of our new image
(tl, tr, br, bl) = rect
widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

# ...and now for the height of our new image
heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))

# take the maximum of the width and height values to reach
# our final dimensions
maxWidth = max(int(widthA), int(widthB))
maxHeight = max(int(heightA), int(heightB))

# construct our destination points which will be used to
# map the screen to a top-down, "birds eye" view
dst = np.array([
    [0, 0],
    [maxWidth - 1, 0],
    [maxWidth - 1, maxHeight - 1],
    [0, maxHeight - 1]], dtype="float32")

# calculate the perspective transform matrix and warp
# the perspective to grab the screen
M = cv2.getPerspectiveTransform(rect, dst)
warp = cv2.warpPerspective(orig, M, (maxWidth, maxHeight))
# convert the warped image to grayscale and then adjust
# the intensity of the pixels to have minimum and maximum
# values of 0 and 255, respectively
warp = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)

# the pokemon we want to identify will be in the top-right
# corner of the warped image -- let's crop this region out
(h, w) = warp.shape
(dX, dY) = (int(w * 0.4), int(h * 0.45))
crop = warp[10:dY, w - dX:w - 10]
cv2.imwrite("cutted.jpg", warp)

# save the cropped image to file(word in the right-top)
#cv2.imwrite("cropped.png", crop)

# show our images
#cv2.imshow("image", img)
#cv2.imshow("warp", warp)



#bhash test
Image_1 = "F:/Python/PythonOpenCV2016052402/Test/5.jpg"  #
Image_2 = 'F:/Python/PythonOpenCV2016052402/cutted.jpg'  #


img_1 = Image.open(Image_1)  # read as color image
img_2 = Image.open(Image_2)
num = b.classfiy_dHash(img_1,img_2)
print(num)

cv2.waitKey(0)
