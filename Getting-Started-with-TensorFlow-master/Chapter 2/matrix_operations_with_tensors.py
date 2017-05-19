# -*- coding: utf-8 -*-
"""
Created on Fri May  5 22:16:30 2017

goal of code: matrix_operations_with_tensors
@author: tony
"""
import tensorflow as tf
import numpy as np
#STEP 1 --- PREPARE THE DATA
matrix1 = np.array([(2,2,2),(2,2,2),(2,2,2)],dtype='float64')
matrix2 = np.array([(1,1,1),(1,1,1),(1,1,1)],dtype='float64')
matrix3 = np.array([(2,7,2),(1,4,2),(9,0,2)],dtype='float64')
print("matrix1=",'\n',matrix1)
print("matrix2=",'\n',matrix2)
print("matrix3=",'\n',matrix3)

ts_matrix1 = tf.constant(matrix1)
ts_matrix2 = tf.constant(matrix2)
ts_matrix3 = tf.constant(matrix3)
#STEP 2 --- DEFINE THE OPERATIONS 
matrix_matmul = tf.matmul(ts_matrix1, ts_matrix2)
#matrix_mul = tf.mul(ts_matrix1, ts_matrix2)
matrix_sum = tf.add(ts_matrix1, ts_matrix2)
matrix_det = tf.matrix_determinant(ts_matrix3)
#STEP 3 --- RUN OPERATIONS 
with tf.Session() as sess:
    result1 = sess.run(matrix_matmul)
    #result2 = sess.run(matrix_mul) 
    result3 = sess.run(matrix_sum)
    result4 = sess.run(matrix_det)

print("matrix_matmul=",'\n',result1)
#print("matrix_mul=",'\n',result2)
print("matrix_sum=",'\n',result3)
print("matrix_det=",'\n',result4)

