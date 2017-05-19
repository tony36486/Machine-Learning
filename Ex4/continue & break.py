# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:53:48 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:continue & break
"""
#利用數值的迴圈控制
a = True
while a:
    b = input('type somthing')
    if b == '1':
        a = False
    else:
        print('still in while 1')
        pass
    
print('finish run 1')
    
#利用 continue & break 的迴圈控制   
while True:
    b = input('type somting')
    if b == '1':
        break #or continue
    else:
        print('still in while 2')
        pass
    
print('finish run 2')
        
