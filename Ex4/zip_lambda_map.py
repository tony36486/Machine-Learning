# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 18:43:25 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:zip、lambda、map
"""
#zip
print("start zip")
a = [1, 2, 3]
b = [4, 5, 6]
print(list (zip(a,b)))
for i, j in zip(a,b):
    print(i,j)

#lambda
print("start lambda")
func = lambda x,y:x+y
print(func(1,2))
"""
def func (x,y):
    return (x+y) 
"""

#map
print("start map")
print(list(map(func, a, b)))
