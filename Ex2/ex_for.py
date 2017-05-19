# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 01:40:19 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:for
"""
#for sample code 1
print('sample code1')
example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]
for i in example_list:
    print(i, end = ' ')
    print('inner of for')
print('outer of for')

#for sample code 2
print('\nsample code2')
for i in range(1,10):
    print(i, end = ' ')
print()
    
for i in range(1,10,2):
    print(i, end = ' ')