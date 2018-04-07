#!/usr/local/bin/python3

import cv2
import numpy as np

# reads a 3d numpy array of bgr values
img = cv2.imread("starrynight.jpg")

px = img[100,100]
print(px)

img[100,100] = [255,255,255]

px = img[100,100]
print(px)

# access RED value
# img.item is preferred way to acces individual pixels
img.itemset((10,10,2),100)
print(img.item(10,10,2))
