#!/usr/local/bin/python3

from keras.models import Model
from keras.layers import Input, Dense, Flatten
from keras.optimizers import SGD
from keras.utils import plot_model
from keras.utils import np_utils

import numpy as np
import pandas as pd
import os
import sys

from utils import mk_dir, load_data

input_shape = (64, 64, 3) # 64 x 64 x 3 images

x = Input(shape=(input_shape)) # input layer
shared = Dense(32)(x) # 32 node dense layer
sub1 = Dense(16)(shared)
sub2 = Dense(16)(shared)
sub3 = Dense(16)(shared)

f1 = Flatten()(sub1)
f2 = Flatten()(sub2)
f3 = Flatten()(sub3)

out1 = Dense(
    units=2,
    activation="softmax"
    )(f1)
out2 = Dense(
    units=117,
    activation="softmax"
    )(f2)
out3 = Dense(
    units=5,
    activation="softmax"
    )(f3)

model = Model(inputs=x, outputs=[out1, out2, out3])
sgd = SGD(lr=1, momentum=0.9, nesterov=True)
model.compile( # compile model
    optimizer=sgd,
    loss=["categorical_crossentropy", "categorical_crossentropy", "categorical_crossentropy"],
    metrics=['accuracy']
)

# visualize, summarize and save model
plot_model(model, to_file='model.png')
model.summary()
print("Saving model...")
mk_dir("models")
with open(os.path.join("models", "kerasFunctionalModel.json"), "w") as f : f.write(model.to_json())

# load training data
print("Loading data...")
image, gender, age, ethnicity, image_size = load_data("./dage.mat")

# convert labels to truth vectors
X_data = image
y_data_g = np_utils.to_categorical(gender, 2)
y_data_a = np_utils.to_categorical(age, 117)
y_data_e = np_utils.to_categorical(ethnicity, 5)

# print shapes
print("Shapes of : image, gender, age, ethnicity...")
print(image.shape) # num x 64 x 64 x 3
print(gender.shape) # num x 1 : 0-1
print(age.shape) # num x 1 : 0-116
print(ethnicity.shape) # num : 0-4

# train
print("Running training...")
data_num = len(X_data) # number of samples
indexes = np.arange(data_num) # ordered indices
np.random.shuffle(indexes) # shuffle
train_num = int(data_num * (0.8)) # training set size

# fetch data and labels in the new shuffled order
X_data = X_data[indexes]
y_data_g = y_data_g[indexes]
y_data_a = y_data_a[indexes]
y_data_e = y_data_e[indexes]

# train / test splits
X_train = X_data[:train_num]
X_test = X_data[train_num:]
y_train_g = y_data_g[:train_num]
y_test_g = y_data_g[train_num:]
y_train_a = y_data_a[:train_num]
y_test_a = y_data_a[train_num:]
y_train_e = y_data_e[:train_num]
y_test_e = y_data_e[train_num:]

# fit model
hist = model.fit(
    X_train, [y_train_g, y_train_a, y_train_e],
    batch_size=32,
    epochs=10,
    # callbacks=callbacks,
    validation_data=(X_test, [y_test_g, y_test_a, y_test_e]))

# save final weights
# print("saving weights")
# model.save_weights(os.path.join("models", "kerasFunctionalModel.h5".format(depth, k)), overwrite=True)
# pd.DataFrame(hist.history).to_hdf(os.path.join("models", "kerasFunctionalModel.h5"), "history")
