# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 21:10:34 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:numpy array copy and deep copy
"""
import numpy as np
A = np.arange(4)
B = A
C = A
D = B
print(A, '\n', B, '\n', C, '\n',D)
A[0] = 4
print(A, '\n', B, '\n', C, '\n',D)
print(A is B, '\n',A is C, '\n',A is D)

B = A.copy()
C = A.copy()
D = B.copy()
print(A, '\n', B, '\n', C, '\n',D)
A[0] = 4
print(A, '\n', B, '\n', C, '\n',D)
print(A is B, '\n',A is C, '\n',A is D)

