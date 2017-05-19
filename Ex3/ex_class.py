# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:05:04 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:class
"""
class Calculator:
   
    def __init__(self, vender, name = 'Good calculator', price = 18):
        self.vender = vender
        self.name = name
        self.price = price
        
    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    
    def minus(self,x,y):
        result = x - y
        print(result)
    
    def times(self,x,y):
        result = x * y
        print(result)
        
    def divide(self,x,y):
        result = x / y
        print(result)
        
