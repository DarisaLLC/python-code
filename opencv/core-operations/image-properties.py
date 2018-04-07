#!/usr/local/bin/python3

import cv2
import numpy as np

# numpy array
img = cv2.imread("starrynight.jpg")

print(type(img))
print(img.size)
print(img.dtype)
