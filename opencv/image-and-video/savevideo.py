#!/usr/local/bin/python3
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# define the codec and create VideoWriter object
# fourcc is a four byte code which specifies the codec
# the codec refers to the encoding and decoding format
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('flippedwebcam.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
