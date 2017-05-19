# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 23:08:01 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:while
"""

"""
python沒有{}，那如何定義while的有效範圍?
利用縮排就能控制

"""
c = 1
while c < 10:
    print(c)
    c = c + 1    
print(c)


"""
邏輯結構控制上，python仍然能使用break、continue
"""
i = 1
j = 1
while i <= 9:
    if i == 8:
        break
    
    while j <= 9:
        if j == 4:
            j += 1
            continue
        
        print(i*j,end = " ")
        j += 1
        
    i += 1
    j = 1
    print()