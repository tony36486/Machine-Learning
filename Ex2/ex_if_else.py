# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:58:36 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:if else
"""
#ex 1
x = 1
y = 2
z = 3
if x>y:
    print('x > y')

if x<y:
    print('x < y')

if x<y<z:
    print('x < y < z')
    
if x!=y:
    print('x != y') 
    
if x==y or x<y:
    print('x==y or x<y')
    
if x==y and x<y:
    print('x==y and x<y')

#ex2    
if x>y:
    print('x > y')
else:
    print('x < y')
    
#ex3
if x>1:
    print('x > 1')
elif x<1:
    print('x < 1')
else:
    print('x = 1')
    