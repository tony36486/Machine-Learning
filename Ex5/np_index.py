# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:11:12 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:numpy index
"""
import numpy as np
A = np.arange(3,15)
print(A)
for i in range(12):
    print(A[i], end = ' ')
    
A = A.reshape(3,4)
print('\n', A)
#印出row的方式
for i in range(np.shape(A)[0]):
    print('\n', A[i][:]) #利用 : 印出所有值
    for j in range(np.shape(A)[1]): 
        print(A[i][j], end = ' ') # A[i,j] 也可拜訪每的元素
#印出col的方式
print('\n', A.T)
for j in range(np.shape(A.T)[0]):
    print('\n', A.T[j][:]) 
    for i in range(np.shape(A.T)[1]):
        print(A.T[j][i],  end = ' ')

