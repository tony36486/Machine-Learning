# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:30:47 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:multi_dim list
"""
#multi_dim list
multi_dim = [[1,2,3],[4,5,6],[7,8,9]]

for index_a in range(len(multi_dim)):
    for index_b in range(len(multi_dim[index_a])):
        print('index_a:', index_a, ', index_b:', index_b, ', text:',multi_dim[index_a][index_b])
        
print(max(multi_dim[2]))