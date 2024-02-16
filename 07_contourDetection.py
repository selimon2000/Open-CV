import cv2 as cv
import numpy as np

img=cv.imread('openCV/photos/cat.jpg')

grey=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(grey,(3,3), cv.BORDER_DEFAULT)
ret, thresh=cv.threshold(blur, 125, 255, cv.THRESH_BINARY)

canny=cv.Canny(thresh, 155, 175)

contours,hierarchies=cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
 
blank=np.zeros((img.shape[0],img.shape[1],3), dtype='uint8')

cv.drawContours(blank, contours, -1, (0,0,255), 1)

cv.imshow('countoured image', blank)

cv.waitKey(0)