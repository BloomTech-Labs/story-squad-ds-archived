# CNN model for Quickdraw dataset
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from tensorflow import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import BatchNormalization
# from keras.optimizers import SGD
from keras.utils import np_utils
from keras.utils import to_categorical
from keras.models import model_from_json
from get_data import load_dataset


#load_data()
x_train, y_train, x_test, y_test, class_names = load_dataset('data')
num_classes = len(class_names)
image_size = 28

# Reshape and normalize
x_train = x_train.reshape(x_train.shape[0], image_size, image_size, 1).astype('float32')
x_test = x_test.reshape(x_test.shape[0], image_size, image_size, 1).astype('float32')

x_train /= 255.0
x_test /= 255.0

# Convert class vectors to class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# define cnn model
def define_model():

 model = Sequential()
 model.add(Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=x_train.shape[1:]))
 model.add(BatchNormalization())
 model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
 model.add(BatchNormalization())
 model.add(MaxPooling2D((2, 2)))
 model.add(Dropout(0.2))
 model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
 model.add(BatchNormalization())
 model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
 model.add(BatchNormalization())
 model.add(MaxPooling2D((2, 2)))
 model.add(Dropout(0.3))
 model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
 model.add(BatchNormalization())
 model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
 model.add(BatchNormalization())
 model.add(MaxPooling2D((2, 2)))
 model.add(Dropout(0.4))
 model.add(Flatten())
 model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
 model.add(BatchNormalization())
 model.add(Dropout(0.5))
 model.add(Dense(100, activation='softmax'))
 # compile model
 adam = tf.keras.optimizers.Adam(learning_rate=0.001)
 model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['top_k_categorical_accuracy'])
 return model

model = define_model()
print(model.summary())

# Training
model.fit(x = x_train, y = y_train, validation_split=0.1,
            batch_size = 32, verbose=2, epochs=10)


# Testing. Final evaluation of the model
scores = model.evaluate(x_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))


fig = plt.figure()
idx = randint(0, len(x_test))
img = x_test[idx]
plt.imshow(img.squeeze())
pred = model.predict(np.expand_dims(img, axis=0))[0]
# print top five predictions
ind = (-pred).argsort()[:5]
latex = [class_names[x] for x in ind]
print(latex)
# save the prediction
fig.savefig('prediction_result.png', dpi=fig.dpi)

# store the classes
with open('class_names.txt', 'w') as file_handler:
   for item in class_names:
       file_handler.write("{}\n".format(item))


# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
   json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
