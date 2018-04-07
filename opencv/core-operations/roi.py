#!/usr/local/bin/python3

import cv2
import numpy as np

img = cv2.imread("starrynight.jpg")

square = img[280:340, 330:390]
img[0:60, 0:60] = square

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
img_resized = cv2.resize(img, (960, 540))
cv2.imshow('image',img_resized)

print("Press ESC to exit...")
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
