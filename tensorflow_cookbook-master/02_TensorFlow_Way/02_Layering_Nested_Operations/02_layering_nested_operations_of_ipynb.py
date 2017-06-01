# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:57:36 2017

@author: tony
"""
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import os
from tensorflow.python.framework import ops
# Reset graph
ops.reset_default_graph()
#Create a graph session
sess = tf.Session()

#Create the Tensors, Constants, and Placeholders
# Create data to feed in
my_array = np.array([[1., 3., 5., 7., 9.],
                   [-2., 0., 2., 4., 6.],
                   [-6., -3., 0., 3., 6.]])
# Duplicate the array for having two inputs
x_vals = np.array([my_array, my_array + 1])
# Declare the placeholder
x_data = tf.placeholder(tf.float32, shape=(3, 5))
# Declare constants for operations
m1 = tf.constant([[1.],[0.],[-1.],[2.],[4.]])
m2 = tf.constant([[2.]])
a1 = tf.constant([[10.]])

#Declare Operations
# 1st Operation Layer = Multiplication
prod1 = tf.matmul(x_data, m1)
# 2nd Operation Layer = Multiplication
prod2 = tf.matmul(prod1, m2)
# 3rd Operation Layer = Addition
add1 = tf.add(prod2, a1)

#Evaluate and Print Output
for x_val in x_vals:
    print(sess.run(add1, feed_dict={x_data: x_val}))
    
#Create and Format Tensorboard outputs for viewing
# Add summaries to tensorboard  
merged = tf.summary.merge_all(key='summaries')
#check floder 
if not os.path.exists("H:\\my_TFpath\\tensorflowlogs"):
    os.makedirs("H:\\my_TFpath\\tensorflowlogs")
# Initialize graph writer:
my_writer = tf.summary.FileWriter("H:\\my_TFpath\\tensorflowlogs", sess.graph)