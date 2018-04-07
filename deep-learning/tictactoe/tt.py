#!/usr/local/bin/python3

import numpy as np # linear algebra library, e.g. matrices
import pandas as pd  # data processing, e.g. read from csv
import sys as sys # exit()

# sklearn machine learning library, e.g. label/one-hot encoding, train/test split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# keras sequential model and fully connected layer
from keras.models import Sequential
from keras.layers import Dense

# load dataset from csv
dataset = pd.read_csv('tic-tac-toe.csv')
X = dataset.iloc[:, 0:9].values # retrieve feature matrix (m x 9)
y = dataset.iloc[:, 9:10].values # retrieve truth matric (m x 1)

# categorical variables (x, o, b) to integer (0, 1, 2)
labelencoder_X = LabelEncoder()
for _ in range(9):
    X[:, _] = labelencoder_X.fit_transform(X[:, _])

# one-hot encode all dependent categorical variables
# changes each integer label into a (3 x 1) binary vector
# todo : what is categorical_features
onehotencoder = OneHotEncoder(categorical_features = [0,1,2,3,4,5,6,7,8])
X = onehotencoder.fit_transform(X).toarray() # (957 x 9) to (957 x 27)

# remove every third column to avoid dummy variable trap
# only need 2 bits to represent 3 possibilities (100 becomes 00)
X = np.delete(X, [0,3,6,9,12,15,18,21,24], axis=1) # (957 x 18)

# encode truth categorical variable
labelencoder_y = LabelEncoder()
y[:, 0] = labelencoder_y.fit_transform(y[:, 0])

# train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# build keras model
model = Sequential()

# add first hidden layer (and input layer)
model.add(Dense(units=9, kernel_initializer='uniform', activation='relu', input_dim=18))

# add second hidden layer
model.add(Dense(units=9, kernel_initializer='uniform', activation='relu'))

# add output layer
model.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))

# compile network
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# train network
model.fit(X_train, y_train, batch_size=10, epochs=100)

# predicting the test set results
y_pred = model.predict(X_test)

# print results
print(y_pred)
