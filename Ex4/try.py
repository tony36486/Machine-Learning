# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 18:12:52 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:try
"""
try:
    file=open('error.txt','r+') #預計會報錯的 func
except Exception as e_mage: #如果報錯將錯誤訊息存入 e_mage  
    print(e_mage)
else: #如果沒有錯誤則不執行 except 
    file.write('write something')
    file.close()
