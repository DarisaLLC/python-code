#!/usr/local/bin/python3

import numpy as np
import cv2

# get video handle
cap = cv2.VideoCapture('videoplayback.3gp')

# while there are frames left
while(cap.isOpened()):

    # read frame
    ret, frame = cap.read()

    # get black and white image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # show frame with 1ms between variable_match
    # press q to quit
    cv2.imshow('frame',gray)

    # waitkey returns the ascii value of the key pressed, unless the time expires in which case it returns False
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release camera and destroy all opencv windows
cap.release()
cv2.destroyAllWindows()
