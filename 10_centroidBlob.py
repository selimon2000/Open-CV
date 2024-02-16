import cv2 as cv
import numpy as np

img=cv.imread('openCV/photos/cat.jpg')

blur=cv.GaussianBlur(img,(9,9), cv.BORDER_DEFAULT)

# convert image to grayscale image
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# convert the grayscale image to binary image
ret,thresh = cv.threshold(gray_image,127,255,0)

#FINDING CENTROID OF BINARY BLOB
# calculate moments of binary image
M = cv.moments(thresh)
# calculate x,y coordinate of center
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
# put text and highlight the center
cv.circle(img, (cX, cY), 5, (255, 255, 255), -1)

# display the image
cv.imshow("Image", img)
cv.waitKey(0)