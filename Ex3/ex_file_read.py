# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:58:36 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:file io read
"""
file = open('my_file.txt', 'r')
content = file.read()
print(content)
file.close()

file = open('my_file.txt', 'r')
content = file.readline()
print(content)
content = file.readline()
print(content)
file.close()

file = open('my_file.txt', 'r')
content = file.readlines()
print(content)
file.close()