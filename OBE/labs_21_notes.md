# Wrap-up Notes from the Labs 21 Data Science Team

The state of Story Squad project at the end of Labs 21 and suggestions for further work.


## The Image Recognition Model

For our first canvas, the DS team (Labs  21) built the image recognition model to classify the drawings that kids upload to Story Squad app. Deep learning models, like convolutional neural network (CNN, or ConvNet) and recurrent neural network (RNN) are suitable to solve our problem. The CNN models are mostly developed and used for computer vision tasks. The Long short-term memory (LSTM) model is a RNN architecture commonly used for handwriting and sketchers recognition. Going further, also a combination of CNN and LSTM can be used to build an image captioning model, it is another interesting solution for the drawings competitions. Or a yolov3 model could be used also and trained with the drawings dataset, using transfer learning techniques.
Our CNN model was trained with quickdraw dataset (using 100 categories) and the accuracy obtained was 94.81% for 10 epochs. The batch normalization layers were used to accelerate the CNN training by reducing internal covariate shift. The dropout layers were used to prevent the model from overfitting.

The python scripts:

- download_subset.py  
This script download_subset.py makes the folder data and downloads a subset from quickdraw dataset from google cloud with 100 categories

- download_dataset.py   
It makes the folder tensorflow_datasets and downloads the full quickdraw dataset from google cloud with 345 categories.

- get_dataset.py
The function load_dataset loads the dataset, the labels, shuffle the data and split the data

- train_cnn.py  
It uses function load_dataset from get_dataset.py to load the dataset, preprocess the dataset, train the model, evaluate the model, print training metrics, print the final evaluation (accuracy),  print the top five prediction labels, return the image of the top prediction and save it as a picture (prediction_result.png), serializes the model to json format, serializes weights to HDF5, saves the serialized model and and weights.

- load_model_predict.py
It loads the model.json and the weights into the model. The function load_image loads and prepares the image.
Then the model makes prediction with one sample (the drawing uploaded to the app)

In the following [folder](https://github.com/Lambda-School-Labs/story-squad-ds/tree/master/Image_Recognition_Model) you can find:
- python scripts
- serialized model and weights (model.json and model.h5)
- screenshots of anaconda prompt with printed training metrics, final evaluation (accuracy), and top five prediction labels
- the image of top prediction (prediction_result.png)

First Canvas and resources:
[here](https://www.notion.so/v3-0-Release-Canvas-Image-Recognition-4b14dc054feb4478ab64e1619bf08835 )
