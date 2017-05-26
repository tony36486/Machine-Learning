# -*- coding: utf-8 -*-
"""
Created on Tue May 23 20:35:17 2017

This script introduces various ways to create tensors in TensorFlow
@author: tony
"""
import tensorflow as tf
from tensorflow.python.framework import ops
ops.reset_default_graph()
"""
Start a graph session
"""
sess = tf.Session()
"""
Creating Tensors
"""
my_tensor = tf.zeros([1,20])
sess.run(my_tensor)
my_var = tf.Variable(tf.zeros([1,20]))
sess.run(my_var.initializer)
print(sess.run(my_var))
row_dim = 2
col_dim = 3
zero_var = tf.Variable(tf.zeros([row_dim, col_dim]))
ones_var = tf.Variable(tf.ones([row_dim, col_dim]))
sess.run(zero_var.initializer)
sess.run(ones_var.initializer)
print(sess.run(zero_var))
print(sess.run(ones_var))
"""
Creating Tensors Based on Other Tensor's Shape
"""
zero_similar = tf.Variable(tf.zeros_like(zero_var))
ones_similar = tf.Variable(tf.ones_like(ones_var))
sess.run(ones_similar.initializer)
sess.run(zero_similar.initializer)
print(sess.run(ones_similar))
print(sess.run(zero_similar))
"""
Filling a Tensor with a Constant
"""
fill_var = tf.Variable(tf.fill([row_dim, col_dim], -1))
sess.run(fill_var.initializer)
print(sess.run(fill_var))

# Create a variable from a constant
const_var = tf.Variable(tf.constant([8, 6, 7, 5, 3, 0, 9]))

# This can also be used to fill an array:
const_fill_var = tf.Variable(tf.constant(-1, shape=[row_dim, col_dim]))
sess.run(const_var.initializer)
sess.run(const_fill_var.initializer)
print(sess.run(const_var))
print(sess.run(const_fill_var))
"""
Creating Tensors Based on Sequences and Ranges
"""
# Linspace in TensorFlow
linear_var = tf.Variable(tf.linspace(start=0.0, stop=1.0, num=3)) # Generates [0.0, 0.5, 1.0] includes the end

# Range in TensorFlow
sequence_var = tf.Variable(tf.range(start=6, limit=15, delta=3)) # Generates [6, 9, 12] doesn't include the end

sess.run(linear_var.initializer)
sess.run(sequence_var.initializer)

print(sess.run(linear_var))
print(sess.run(sequence_var))
"""
Random Number Tensors
"""
rnorm_var = tf.random_normal([row_dim, col_dim], mean=0.0, stddev=1.0)
runif_var = tf.random_uniform([row_dim, col_dim], minval=0, maxval=4)

print(sess.run(rnorm_var))
print(sess.run(runif_var))
"""
Visualizing the Variable Creation in TensorBoard
"""
# Reset graph
ops.reset_default_graph()

# Start a graph session
sess = tf.Session()

# Create variable
my_var = tf.Variable(tf.zeros([1,20]))

# Add summaries to tensorboard
merged = tf.summary.merge_all()

# Initialize graph writer:
writer = tf.summary.FileWriter("H:\\my_TFpath\\tensorlogs", graph=sess.graph)

# Initialize operation
initialize_op = tf.global_variables_initializer()

# Run initialization of variable
sess.run(initialize_op)
