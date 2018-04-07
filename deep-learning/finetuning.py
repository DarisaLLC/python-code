#!/usr/local/bin/python3

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.utils import to_categorical
import os
from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.applications import VGG16

from keras import models
from keras import layers
from keras import optimizers

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
model.add(layers.Dense(3, activation='softmax'))

# summary
model.summary()

# collect training and validation batches
train_datagen = ImageDataGenerator(
      rescale=1./255,
      rotation_range=20,
      width_shift_range=0.2,
      height_shift_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')
validation_datagen = ImageDataGenerator(rescale=1./255)
train_batchsize = 100
val_batchsize = 10
train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(image_size, image_size),
        batch_size=train_batchsize,
        class_mode='categorical')
validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(image_size, image_size),
        batch_size=val_batchsize,
        class_mode='categorical',
        shuffle=False)

# compile
model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])
# train
history = model.fit_generator(
      train_generator,
      steps_per_epoch=train_generator.samples/train_generator.batch_size ,
      epochs=30,
      validation_data=validation_generator,
      validation_steps=validation_generator.samples/validation_generator.batch_size,
      verbose=1)

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
