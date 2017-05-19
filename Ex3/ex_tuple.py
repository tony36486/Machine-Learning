# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:02:23 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:tuple
#both are compose with continuous order elements
"""
tuple_a = (1, 'Taiwan', 'good people')

for content in tuple_a:
    print(content)
 
 #訪問list內容   
for index in range(len(tuple_a)):
    print('index:', index, ', content in list:', tuple_a[index])
    
for index in range(len(tuple_a)):
    index = -1*(index + 1)
    print('index:', index, ', content in list:', tuple_a[index])
"""  
#添加List內容
print(tuple_a)
tuple_a.insert(0,'test')
print(tuple_a)
tuple_a.insert(-1,'test')
print(tuple_a)
tuple_a.append('test')
print(tuple_a)"""
#訪問不只一個list內容
for index in range(len(tuple_a)):
    print('index:', index, ', content in list:', tuple_a[index])
    
for index in range(len(tuple_a)):
    index = -1*(index + 1)
    print('index:', index, ', content in list:', tuple_a[index])    
print(tuple_a[2:4])
print(tuple_a[-5:-3])
#統計list
print('total test :',tuple_a.count('test'))
"""
#移除值
print(tuple_a)
tuple_a.remove('test')
print(tuple_a)
tuple_a.remove('test')
print(tuple_a)
tuple_a.remove('test')
print(tuple_a)
"""
"""
#變更值
tuple_a[0] = 'NO1'
print(tuple_a)
"""