# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:58:36 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:file io write
"""
file_test = "my file text\n"
append_text = "my append text\n"
#開啟文件
my_file = open('my_file.txt','w')
#寫入內容
my_file.write(file_test)
#關閉文件
my_file.close()

#開啟文件
my_file = open('my_file.txt','a')
#寫入內容
my_file.write(append_text)
#關閉文件
my_file.close()
