import cv2 as cv

img=cv.imread('openCV/photos/cat.jpg')

#colour changing
b,g,r = cv.split(img)
cv.imshow('B', b)
cv.imshow('R', r)
cv.imshow('G', g)



cv.waitKey(0)