#!/usr/local/bin/python3

import numpy as np
import cv2

# start first camera device
cap = cv2.VideoCapture(0)

while(True):
    # read video frame by frame
    ret, frame = cap.read()

    # collect frame as grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display each frame
    # 1 ms wait allows the video to play without much delay
    # yet pressing the q key will quit on the next iteration
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the camera
cap.release()
cv2.destroyAllWindows()
