#!/usr/local/bin/python3

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.utils import to_categorical
import os
import sys
from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.applications import VGG16
from utils import load_data
from keras import models
from keras import layers
from keras import optimizers
from keras.utils import np_utils
from keras.layers.convolutional import AveragePooling2D
from keras.layers.normalization import BatchNormalization

train_dir = "./clean-dataset/train"
validation_dir = "./clean-dataset/validation"

image_size = 224 
vgg_conv = VGG16(weights='imagenet', include_top=False, input_shape=(image_size, image_size, 3))

# freeze early layers and only train the last 4 of the feature extractor
for layer in vgg_conv.layers[:-4]:
    layer.trainable = False
for layer in vgg_conv.layers:
    print(layer, layer.trainable)

# custom model
model = models.Sequential()

# use partial vgg
model.add(vgg_conv)

# add relu and softmax
model.add(layers.Flatten())
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dropout(0.5))

# todo : multiple softmax classifiers
model.add(layers.Dense(2, activation='softmax'))
model.add(layers.Dense(117, activation='softmax'))
model.add(layers.Dense(5, activation='softmax'))

# summary
model.summary()

# todo1 : collect training and validation sets
image, gender, age, ethnicity, image_size = load_data("dage.mat")
print("shapes of : image, gender, age, ethnicity")
print(image.shape) # num x 64 x 64 x 3
print(gender.shape) # num : 1 or 0
print(age.shape) # num : 0-116
print(ethnicity.shape) # num : 0-4

X_data = image
y_data_g = np_utils.to_categorical(gender, 2)
y_data_a = np_utils.to_categorical(age, 117)
y_data_e = np_utils.to_categorical(ethnicity, 5)

# debug
sys.exit()

# compile
model.compile(loss=["categorical_crossentropy",
              "categorical_crossentropy",
              "categorical_crossentropy"],
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])

# todo2 : train

# save weights
model.save('small_last4.h5')

# create a generator for prediction
validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(image_size, image_size),
        batch_size=val_batchsize,
        class_mode='categorical',
        shuffle=False)

fnames = validation_generator.filenames # get the filenames from the generator
ground_truth = validation_generator.classes # get the ground truth from generator
label2index = validation_generator.class_indices # get the ground truth from generator
idx2label = dict((v,k) for k,v in label2index.items()) # getting the mapping from class index to class label

# get the predictions from the model using the generator
predictions = model.predict_generator(
    validation_generator,
    steps=validation_generator.samples/validation_generator.batch_size,
    verbose=1)
predicted_classes = np.argmax(predictions,axis=1)

# print validation accuracy
errors = np.where(predicted_classes != ground_truth)[0]
print("No of errors = {}/{}".format(len(errors),validation_generator.samples))
