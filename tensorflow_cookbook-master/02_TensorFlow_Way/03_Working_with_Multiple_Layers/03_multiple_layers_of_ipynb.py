# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:52:07 2017

@author: tony
"""
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import os
from tensorflow.python.framework import ops
#Reset graph
ops.reset_default_graph()

#Create a Graph Session
sess = tf.Session()

#Create Tensors
# Create a small random 'image' of size 4x4
x_shape = [1, 4, 4, 1]
x_val = np.random.uniform(size=x_shape)

#Create the Data Placeholder
x_data = tf.placeholder(tf.float32, shape=x_shape)

#First Layer: Moving Window (Convolution)
# Create a layer that takes a spatial moving window average
# Our window will be 2x2 with a stride of 2 for height and width
# The filter value will be 0.25 because we want the average of the 2x2 window
my_filter = tf.constant(0.25, shape=[2, 2, 1, 1])
my_strides = [1, 2, 2, 1]
mov_avg_layer= tf.nn.conv2d(x_data, my_filter, my_strides,
                            padding='SAME', name='Moving_Avg_Window')

#Second Layer: Custom
# Define a custom layer which will be sigmoid(Ax+b) where
# x is a 2x2 matrix and A and b are 2x2 matrices
def custom_layer(input_matrix):
    input_matrix_sqeezed = tf.squeeze(input_matrix)
    A = tf.constant([[1., 2.], [-1., 3.]])
    b = tf.constant(1., shape=[2, 2])
    temp1 = tf.matmul(A, input_matrix_sqeezed)
    temp = tf.add(temp1, b) # Ax + b
    return(tf.sigmoid(temp))
# Add custom layer to graph
with tf.name_scope('Custom_Layer') as scope:
    custom_layer1 = custom_layer(mov_avg_layer)
    
#Run Output
print(sess.run(mov_avg_layer, feed_dict={x_data: x_val}))
print(sess.run(custom_layer1, feed_dict={x_data: x_val}))

#Create and Format Tensorboard outputs for viewing
# Add summaries to tensorboard  
merged = tf.summary.merge_all(key='summaries')
#check floder 
if not os.path.exists("H:\\my_TFpath\\tensorflowlogs"):
    os.makedirs("H:\\my_TFpath\\tensorflowlogs")
# Initialize graph writer:
my_writer = tf.summary.FileWriter("H:\\my_TFpath\\tensorflowlogs", sess.graph)