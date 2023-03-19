#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas
import numpy
from sklearn.model_selection import train_test_split
import tensorflow

import matplotlib.pyplot as plt
import nltk
from tkinter import *
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
import scipy
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds
from tensorflow.python import keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

data=pandas.read_csv('WordList.csv')
X=data['Negative Sense Word List']
y=data['Positive Sense Word List']
X_train,X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=0, shuffle=True)

original_train_data, original_validation_data, original_test_data = tfds.load(
    name="WordList.csv", 
    split=('train[:60%]', 'train[60%:]', 'test'),
    as_supervised=True)




# %%
