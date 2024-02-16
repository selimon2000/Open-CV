import cv2 as cv

img=cv.imread('openCV/photos/cat.jpg')
height, width, channels = img.shape

print("height:", height)
print("width:", width)

newImg=img[int(height/2):height, 0:width]

cv.imshow('cat', img)
cv.imshow('newCat', newImg)

cv.waitKey(0)