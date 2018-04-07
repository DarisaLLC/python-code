#!/usr/local/bin/python3

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('digits.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(type(gray))
print(gray.shape)

# image is 1000 x 2000
# now we split the image to 5000 cells with each 20x20
# for loop can be used to create lists within the square brackets
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
# print(cells[0][0][0])

# nump array with size (50,100,20,20)
x = np.array(cells)

# prepare train_data and test_data
train = x[:,:50].reshape(-1,400).astype(np.float32) # size = (2500,400)
print(train.shape)

test = x[:,50:100].reshape(-1,400).astype(np.float32) # size = (2500,400)

# create labels for train and test data
k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis] # converts list to array with 2500 x 1 shape

test_labels = train_labels.copy()

# train and analyze
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret,result,neighbours,dist = knn.findNearest(test,k=5)

# verify accuracy
# compare the result with test_labels and check which are wrong
matches = result == test_labels # matrix of results
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print (accuracy)
