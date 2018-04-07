#!/usr/local/bin/python3

import numpy as np # linear algebra (matrices)
import pandas as pd # data manipulation (e.g. csv)

# machine learning library
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix  # ?

# deep learning library
# using simple feed forward network design
from keras.models import Sequential
from keras.layers import Dense

# import dataset
dataset = pd.read_csv("tic-tac-toe.csv")
X = dataset.iloc[:, 0:9].values # cell values
y = dataset.iloc[:, 9:10].values # result

# integer encode cell values
# integer encoding determined by sklearn automatically
labelencoder_X = LabelEncoder()
for _ in range(9):
    X[:, _] = labelencoder_X.fit_transform(X[:, _])

# one hot encode all dependent categorical variables
onehotencoder = OneHotEncoder(categorical_features = [0,1,2,3,4,5,6,7,8])
X = onehotencoder.fit_transform(X).toarray()
print(X)

# Remove every third column to avoid dummy variable trap
# Only need 2 bits to represent 3 possibilities
X = np.delete(X, [0,3,6,9,12,15,18,21,24], axis=1)

# encode target categorical variable
labelencoder_y = LabelEncoder()
y[:, 0] = labelencoder_y.fit_transform(y[:, 0])

# split train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize neural network
model = Sequential()

# Add first hidden layer (and input layer)
model.add(Dense(units=9, kernel_initializer='uniform', activation='relu', input_dim=18))

# Add second hidden layer
model.add(Dense(units=9, kernel_initializer='uniform', activation='relu'))

# Add output layer
model.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))

# Compile network
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train network
model.fit(X_train, y_train, batch_size=10, epochs=100)

# Predicting the test set results
y_pred = model.predict(X_test)
