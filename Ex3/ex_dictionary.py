# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:10:06 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:dictionary
"""
def test_func():
    print("function running")
    return "function result"
    

dic = {'apple':1, 'boy':2, 'cat':3, 'dog':4, 4:'four', 'func':test_func()}
print(dic)
print(dic['apple'])
print(dic['boy'])
print(dic['cat'])
print(dic['dog'])
print(dic[4])
print(dic['func'])
test_func()
