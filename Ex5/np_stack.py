# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:28:53 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:numpy array stack
"""
import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])
print(A.shape)
C = np.vstack((A,B))  #vertical stack
D = np.hstack((A,B))  #horizontal stack

print(C, '\n', C.shape)
print(C.T, '\n', C.T.shape)
#shape要符合矩陣在數學上的邏輯，才能轉置
print(D, '\n', D.shape)
print(D.T, '\n', D.T.shape)
print(D, '\n',D[np.newaxis, :].shape)
print(D[np.newaxis, :].T, '\n', D[np.newaxis, :].T.shape)

#multi-stack
E = np.concatenate((A[np.newaxis, :],B[np.newaxis, :],B[np.newaxis, :],A[np.newaxis, :]), axis=0)
print(E, '\n', E.shape)
F = np.concatenate((A[np.newaxis, :],B[np.newaxis, :],B[np.newaxis, :],A[np.newaxis, :]), axis=1)
print(F, '\n', F.shape)

