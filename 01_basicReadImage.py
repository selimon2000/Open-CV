import cv2 as cv

img=cv.imread('openCV/photos/cat.jpg')
cv.imshow('cat', img)

img=cv.imread('openCV/photos/dog.jpg')
cv.imshow('dog', img)
 
cv.waitKey(0)