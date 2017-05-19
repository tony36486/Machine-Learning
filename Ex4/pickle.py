# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 22:29:44 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:pickle
"""
import pickle
#write a pickle file
#'''
a_dict = {'number':1, 'list':['me', 405216258], 'dist':{'lab':'b05'}}
file = open('pickle_example.pickle','wb')
pickle.dump(a_dict,file)
file.close()
#'''
#read a pickle file
#'''
file = open('pickle_example.pickle','rb')
b_dict = pickle.load(file)
file.close()
print(b_dict)
#'''
