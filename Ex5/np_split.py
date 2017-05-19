# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:58:29 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:numpy array split
"""
import numpy as np
A = np.arange(12).reshape(3,4)
print(A)
# 橫向分割
print(np.split(A, 3, axis=0))
print(np.vsplit(A, 3))
# 縱向分割 
print(np.split(A, 4, axis=1))
print(np.hsplit(A, 4))
"""
split()、vsplit()、hsplit()不允許不等量的分割
print(np.split(A, 4, axis=0))
print(np.vsplit(A, 4))
print(np.split(A, 3, axis=1))
print(np.hsplit(A, 3))
是不被允許的
"""
print(np.array_split(A, 4, axis=0))
print(np.array_split(A, 3, axis=1))

