from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from scripts.preprocessing import preprocessing

def main():
	# creates data.txt file with training/validation data
	preprocessing()

if __name__=='__main__':
	main()