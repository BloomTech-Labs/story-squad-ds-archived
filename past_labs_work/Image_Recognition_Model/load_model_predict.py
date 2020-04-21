import os
import sys
import numpy as np
from PIL import Image
import tensorflow as tf
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import BatchNormalization
from keras.optimizers import SGD
from keras.utils import np_utils
from keras.models import model_from_json
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from keras.models import load_model

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")

# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(28, 28))
	img = img_to_array(img)
	# reshape into a single sample with 1 channel
	img = img.reshape(1,28,28, 1).astype('float32')
	img = img / 255.0
	return img


sample_image  = 'IMG.jpg' # 1 sample
# load an image and predict
img = load_image(sample_image)
# result = model.predict_class(img)
result = loaded_model.predict(img)
print(result[0])
