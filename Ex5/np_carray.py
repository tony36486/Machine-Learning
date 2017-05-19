# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:37:40 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:numpy creat array
"""
import numpy as np
#定義元素變數型態與更動
my_array = np.array([[1,2,3],[4,5,6]],dtype=np.float) #int 整數  #float 小數
print(my_array.dtype)
my_array.dtype = np.int
print(my_array.dtype)
#定義0矩陣
zero_array = np.zeros((3,4))
print(zero_array)
#定義1矩陣
one_array = np.ones((3,4))
print(one_array)
#定義空矩陣
null_array = np.empty((3,4))
print(null_array)
#定義有序矩陣
range_array = np.arange(12)
print(range_array)
range_array = np.arange(12).reshape((3,4))
print(range_array)
range_array = np.arange(10,22)
print(range_array)
range_array = np.arange(10,22).reshape((3,4))
print(range_array)
#定義等差矩陣
line_array = np.linspace(1, 12, 12)
print(line_array)
line_array = np.linspace(1, 12, 12).reshape((3,4))
print(line_array)

