# -*- coding: utf-8 -*-
"""
Created on Tue May 23 23:11:48 2017

This function introduces how to use placeholders in TensorFlow
@author: tony
"""
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops
ops.reset_default_graph()
sess = tf.Session()
"""
sess = tf.Session()
"""
x = tf.placeholder(tf.float32, shape=(4, 4))
# Input data to placeholder, note that 'rand_array' and 'x' are the same shape.
rand_array = np.random.rand(4, 4)

# Create a Tensor to perform an operation (here, y will be equal to x, a 4x4 matrix)
y = tf.identity(x)

# Print the output, feeding the value of x into the computational graph
print(sess.run(y, feed_dict={x: rand_array}))

merged = tf.summary.merge_all()
writer = tf.summary.FileWriter("H:\\my_TFpath\\placeholder_logs", sess.graph)