#!/usr/local/bin/python3

import keras
import numpy as np
from keras.applications import vgg16, inception_v3, resnet50, mobilenet

# load some imagenet models
vgg_model = vgg16.VGG16(weights="imagenet")
inception_model = inception_v3.InceptionV3(weights="imagenet")
resnet_model = resnet50.ResNet50(weights="imagenet")
mobilenet_model = mobilenet.MobileNet(weights="imagenet")

# keras pre-processing libraries
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt

# %matplotlib inline


# load image as pil and plot
filename = 'images/donald-trump.jpg'
original = load_img(filename, target_size=(224, 224))
print('PIL image size',original.size)
plt.imshow(original)
plt.show()

# convert to numpy and plot
numpy_image = img_to_array(original)
print('numpy array size', numpy_image.shape)
plt.imshow(np.uint8(numpy_image))
plt.show()

 # create batch by adding a dimension
image_batch = np.expand_dims(numpy_image, axis=0)
print('image batch size', image_batch.shape)
plt.imshow(np.uint8(image_batch[0]))

# prepare for vgg
processed_image = vgg16.preprocess_input(image_batch.copy())

# predict
predictions = vgg_model.predict(processed_image)

# get imagenet label
label = decode_predictions(predictions)
print(label)
