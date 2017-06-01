# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:36:57 2017

@author: tony
"""
import os
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops
# Reset graph
ops.reset_default_graph()

#Start a graph session
sess = tf.Session()

#Create tensors
# Create data to feed in the placeholder
x_vals = np.array([1., 3., 5., 7., 9.])
# Create the TensorFlow Placceholder
x_data = tf.placeholder(tf.float32)
# Constant for multilication
m = tf.constant(3.)

# Multiplication
prod = tf.multiply(x_data, m)
for x_val in x_vals:
    print(sess.run(prod, feed_dict={x_data: x_val}))
    
# Add summaries to tensorboard    
merged = tf.summary.merge_all(key='summaries')
#check floder 
if not os.path.exists("H:\\my_TFpath\\tensorflowlogs"):
    os.makedirs("H:\\my_TFpath\\tensorflowlogs")
# Initialize graph writer:
my_writer = tf.summary.FileWriter("H:\\my_TFpath\\tensorflowlogs", sess.graph)