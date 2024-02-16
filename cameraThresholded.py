import cv2 as cv
import numpy as np
capture=cv.VideoCapture(0)

while 1:
    isTrue, originalFrame= capture.read()
    frame=cv.GaussianBlur(originalFrame, (7,7), cv.BORDER_DEFAULT)
    frame=cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    minThresh=np.array([101,50,38]) #for colour of blue
    maxThresh=np.array([130,255,255])
    
    # minThresh=np.array([120,100,100]) #for colour of pink
    # maxThresh=np.array([180,255,255])

    frame = cv.inRange(frame, minThresh, maxThresh)

    #FINDING CENTROID OF BINARY BLOB
    # calculate moments of binary image
    M = cv.moments(frame)
    # calculate x,y coordinate of center
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    
    # put text and highlight the center
    cv.circle(originalFrame, (cX, cY), 5, (255, 255, 255), -1)    
    
    cv.imshow('Video', originalFrame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()