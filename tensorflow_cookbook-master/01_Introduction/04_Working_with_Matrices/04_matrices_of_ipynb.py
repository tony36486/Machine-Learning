# -*- coding: utf-8 -*-
"""
Created on Wed May 24 18:34:11 2017

This function introduces various ways to create matrices and how to use them in TensorFlow
@author: tony
"""
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops
ops.reset_default_graph()
#Start a graph session
sess = tf.Session()
"""
Declaring matrices
"""
#Identity Matrix
identity_matrix = tf.diag([1.0,1.0,1.0])
print(sess.run(identity_matrix))
#2x3 constant matrix
B = tf.fill([2,3], 5.0)
print(sess.run(B))
#3x2 random uniform matrix
C = tf.random_uniform([3,2])
print(sess.run(C))
#Create matrix from np array
D = tf.convert_to_tensor(np.array([[1., 2., 3.], [-3., -7., -1.], [0., 5., -2.]]))
print(sess.run(D))
"""
Matrix Operations
"""
#Matrix addition/subtraction
print(sess.run(B+B))
print(sess.run(B-B))
#Matrix Transpose
print(sess.run(tf.transpose(C)))
#Matrix Determinant
print(sess.run(tf.matrix_determinant(D)))
#Matrix Inverse
print(sess.run(tf.cholesky(identity_matrix)))
#Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = sess.run(tf.self_adjoint_eig(D))
print(eigenvalues)
print(eigenvectors)
"""
Visualizing the Variable Creation in TensorBoard
"""
# Reset graph
ops.reset_default_graph()
# Start a graph session
sess = tf.Session()

#graph u want to see


# Add summaries to tensorboard
merged = tf.summary.merge_all()
# Initialize graph writer:
writer = tf.summary.FileWriter("H:\\my_TFpath\\matrices", graph=sess.graph)
# Initialize operation
initialize_op = tf.global_variables_initializer()
# Run initialization of variable
sess.run(initialize_op)