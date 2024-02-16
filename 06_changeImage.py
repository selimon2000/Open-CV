import cv2 as cv

img=cv.imread('openCV/photos/cat.jpg')
cv.imshow('original', img)

#colour changing
# hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

grey=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('greyscale', grey)

#Blurring
# blur=cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# blur=cv.GaussianBlur(img,(9,9), cv.BORDER_DEFAULT)
# cv.imshow('99blur', blur)

# #Edge Cascade:
# canny=cv.Canny(img, 50, 50)
# cv.imshow('Canny Edges', canny)

#Edge Cascade with blur:
# canny=cv.Canny(cv.GaussianBlur(img,(5,5), cv.BORDER_DEFAULT), 50, 50)
# cv.imshow('Canny Edges with blur', canny)

#thresholding image
ret, thresh=cv.threshold(grey, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresholded', thresh)

cv.waitKey(0)