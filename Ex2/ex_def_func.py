# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 21:01:58 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:def
"""

#sample 1

def BMI_Calculate(high = None, weight = None):
    if high == None:
        print('high:採用預設\n')
        high = 170
    if weight == None:
        print('weight:採用預設\n')
        weight = 68
    return BMI_Calculater(high, weight)

def BMI_Calculater(high, weight):
    print('high',high,'weight',weight)
    bmi = weight/((high/100)**2)
    return bmi

print('BMI',BMI_Calculate())

