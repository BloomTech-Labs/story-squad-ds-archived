# downloads a subset from quickdraw dataset with 100 categories
import urllib.request
import os
from os import makedirs

# create directories
dataset_home = 'data/'
makedirs(dataset_home, exist_ok=True)

# Categories names
f = open("class_names.txt","r")
# And for reading use
classes = f.readlines()
f.close()
classes = [c.replace('\n','').replace(' ','_') for c in classes]

def download():
    base = 'https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/'
    for c in classes:
      cls_url = c.replace('_', '%20')
      path = base+cls_url+'.npy'
      print(path)
      urllib.request.urlretrieve(path, 'data/'+c+'.npy')

download()
