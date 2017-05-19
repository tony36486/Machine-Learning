# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:31:03 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:variable
"""
#變數命名規則測試
test = 1

#數字可以餐與變數命名，但不能開頭
#1_test = 1 
test_1 = 1

#一次宣告多個變數
a,b,c = 1,'char',0

#python 中並沒有array,但是有類似的東西叫list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ['a', 'b', 'c', 'd']

#多維度 list 宣告
list_n = [[1 ,2], [3, 4]]
list_plus = [list1, list2]

#直接印出list與array僅印第一位不同，list是全印
print(list1)

#使用[]控制印出項目，使用:控制範圍  注意: 開始印:結束不印
print(list1[0])
print(list1[2:4])

#index 搜尋list
print(list2.index('a'))

#+ 把兩個List給加在一起
print(list1+list2)

#string變數能採用list邏輯
string1 = "I'm_tony"
print(string1[0]+string1[1]+string1[2]+string1[3]+string1[4]+string1[5]+string1[6]+string1[7])
print(string1[0:4]+string1[4:8])

#反斜線作為功能符號，不算入計算
string2 = 'I\'m_tony'
print(string2[0]+string2[1]+string2[2]+string2[3]+string2[4]+string2[5]+string2[6]+string2[7])

#
