# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:54:41 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:numpy attribute
"""
import numpy as np

array = np.array([[1,2,3],
                  [4,5,6]])
    
print(array)
#維度
print('number of dim', array.ndim)
#行數與列數
print('shape:',array.shape)
#元素數目
print('size:',array.size)
