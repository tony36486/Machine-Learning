# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 01:13:07 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:set
"""
char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
setence = "Welcome Back To This Tutorial"

print(type(set(char_list)))
print(set(char_list))
print(type(set(setence)))
print(set(setence))
#set()內不能放入超過1D的list

unique_char = set(char_list)
#於 set 中增加元素,一次只能增加一個元素 
unique_char.add('x')
print(unique_char)

#於set 中刪減元素
unique_char.remove('x')
print(unique_char)

#清空 set
unique_char.clear()
print(unique_char)

#集合處理
set1 = set(char_list)
set2 = {'a', 'e', 'i'}
#不同的元素
print(set1.difference(set2))
print(set2.difference(set1))
#交集的元素
print(set1.intersection(set2))
print(set2.intersection(set1))
