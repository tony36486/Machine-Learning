# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:27:54 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:numpy basic operation 1
"""
import numpy as np
#"""
a = np.array([10,20,30,40])
b = np.arange(4)
print(a,b)
#矩陣相減
c = a-b
print(c)
#矩陣相加
c = a+b
print(c)
#矩陣平方
c = b**2
print(c)
#矩陣判斷
print(b==3)
#矩陣乘法
a = np.array([[1,1],[0,1]])
b = b.reshape((2,2))
print(a,'\n',b)
c = a*b
c_dot = np.dot(a,b)
c_dot_2 = a.dot(b)
print(c)
print(c_dot)
print(c_dot_2)
#"""
#"""
#生成隨機矩陣
a = np.random.random((2,4))
print(a)
print(np.sum(a))
print(np.min(a, axis = 0))
print(np.max(a, axis = 1))
#"""
#"""
#sin cos tan 角度單位 為弧度
print(np.sin(90/360*2*np.pi)) #sin(90度)
print(np.sin(60/360*2*np.pi)) #sin(60度)
print(np.sin(30/360*2*np.pi)) #sin(30度)
print(np.sin(0/360*2*np.pi)) #sin(0度)
print(np.cos(60/360*2*np.pi)) #cos(60度)
print(np.cos(30/360*2*np.pi)) #cos(30度)
print(np.tan(45/360*2*np.pi)) #tan(45度)
#"""

