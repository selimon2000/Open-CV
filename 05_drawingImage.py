import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8')
blank[200:300, 300:400]=0,255,0

cv.rectangle(blank, (0,0), (250,250), (0,255,255), thickness=-1)
cv.putText(blank, 'On Your Left', (250,250), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (100,200,250), 2)

cv.imshow('Green', blank)

cv.waitKey(0)