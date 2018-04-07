#!/usr/local/bin/python3

import numpy as np
import cv2

# read image as grayscale
img = cv2.imread('starrynight.jpg',0)

# show image in named window
cv2.imshow('image',img)

# wait indefinitely for key
k = cv2.waitKey(0)

# ESC to exit
if k == 27:
    cv2.destroyAllWindows()
# s to save and exit
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('graystarrynight.jpg',img)
    cv2.destroyAllWindows()
