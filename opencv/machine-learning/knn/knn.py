#!/usr/local/bin/python3

import cv2
import numpy as np
import matplotlib.pyplot as plt # graph plotting in matlab style

# two dimensional feature space
# feature set containing (x,y) values of 25 known data
trainingData = np.random.randint(0,100,(25,2)).astype(np.float32)

# labels red or blue with numbers 0 and 1
responses = np.random.randint(0,2,(25,1)).astype(np.float32)

print(type(responses))

# plot red triangles
red = trainingData[responses.ravel() == 0]
plt.scatter(red[:,0],red[:,1],80,'r','^')

# plot blue squares
blue = trainingData[responses.ravel() == 1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

# new random data
newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)

# randomly place
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

# knn does not actually require much training, since computation is deferrend until classification
# thus train() in this case probably just populates some internal data structures, like the features space
# find_nearest() will process the list of neighbours
knn = cv2.ml.KNearest_create()
knn.train(trainingData,cv2.ml.ROW_SAMPLE, responses)
ret, results, neighbours ,dist = knn.findNearest(newcomer, 3)

print ("result: ", results,"\n")
print ("neighbours: ", neighbours,"\n")
print ("distance: ", dist)

plt.show()
