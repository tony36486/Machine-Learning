# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:02:23 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:list
#both are compose with continuous order elements
"""
list_a = [1, 'Taiwan', 'good people']

for content in list_a:
    print(content)
 
 #訪問list內容   
for index in range(len(list_a)):
    print('index:', index, ', content in list:', list_a[index])
    
for index in range(len(list_a)):
    index = -1*(index + 1)
    print('index:', index, ', content in list:', list_a[index])
    
#添加List內容
print(list_a)
list_a.insert(0,'test')
print(list_a)
list_a.insert(-1,'test')
print(list_a)
list_a.append('test')
print(list_a)

#訪問不只一個list內容
for index in range(len(list_a)):
    print('index:', index, ', content in list:', list_a[index])
    
for index in range(len(list_a)):
    index = -1*(index + 1)
    print('index:', index, ', content in list:', list_a[index])
    
print(list_a[2:4])
print(list_a[-5:-3])

#統計list
print('total test :',list_a.count('test'))

#移除值
print(list_a)
list_a.remove('test')
print(list_a)
list_a.remove('test')
print(list_a)
list_a.remove('test')
print(list_a)

#變更值
list_a[0] = 'NO1'
print(list_a)