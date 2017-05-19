# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:30:43 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:numpy basic operation 2
"""
import numpy as np
A = np.arange(14,2,-1).reshape((3,4))
print(A)
#min() 找最小值 argmin() 找最小值位置
print(np.argmin(A))
#max() 找最大值 argmax() 找最大值位置
print(np.argmax(A))
#找平均
print(np.mean(A))
print(A.mean())
print(np.average(A))
#print(A.average()) 無法適用
#找中位數
print(np.median(A))
#找項數和
print(np.cumsum(A))
#找相數差
print(np.diff(A))
#找出非0
print(np.nonzero(A)) #輸出 行 與 列
#排序
print(np.sort(A)) #按照逐行排序
#反矩陣
print(np.transpose(A)) #也可使用print((A.T))
#限定矩陣元素範圍
print(np.clip(A,5,9))

