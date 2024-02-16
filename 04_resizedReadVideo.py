import cv2 as cv
 
def rescaleFrame(frame, scale=1.5):
    width =int(frame.shape[1]*scale)
    height =int(frame.shape[0]*scale)
    dimensions=(width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture=cv.VideoCapture(0)

while 1:
    isTrue, frame= capture.read()

    resized_image=rescaleFrame(frame)
    cv.imshow('live camera', resized_image)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()