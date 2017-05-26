# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:57:40 2017

This function introduces various operations in TensorFlow
@author: tony
"""
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops
ops.reset_default_graph()

#Open graph session
sess = tf.Session()

#Arithmetic Operations
print(sess.run(tf.div(3,4)))
print(sess.run(tf.truediv(3,4)))
print(sess.run(tf.floordiv(3.0,4.0)))
print(sess.run(tf.mod(22.0,5.0)))
print(sess.run(tf.cross([1.,0.,0.],[0.,1.,0.])))

#Trig functions
print(sess.run(tf.sin(3.1416)))
print(sess.run(tf.cos(3.1416)))
print(sess.run(tf.div(tf.sin(3.1416/4.), tf.cos(3.1416/4.))))

#Custom operations
test_nums = range(15)

def custom_polynomial(x_val):
    # Return 3x^2 - x + 10
    return(tf.subtract(3 * tf.square(x_val), x_val) + 10)

expected_output = [3*x*x-x+10 for x in test_nums]
print(expected_output)

for num in test_nums:
    print(sess.run(custom_polynomial(num)))
    
"""
Visualizing the Variable Creation in TensorBoard
"""
# Reset graph
ops.reset_default_graph()

# Start a graph session
sess = tf.Session()

#Arithmetic Operations
print(sess.run(tf.div(3,4)))
print(sess.run(tf.truediv(3,4)))
print(sess.run(tf.floordiv(3.0,4.0)))
print(sess.run(tf.mod(22.0,5.0)))
print(sess.run(tf.cross([1.,0.,0.],[0.,1.,0.])))

# Add summaries to tensorboard
merged = tf.summary.merge_all()

# Initialize graph writer:
writer = tf.summary.FileWriter("H:\\my_TFpath\\operations", graph=sess.graph)

# Initialize operation
initialize_op = tf.global_variables_initializer()

# Run initialization of variable
sess.run(initialize_op)