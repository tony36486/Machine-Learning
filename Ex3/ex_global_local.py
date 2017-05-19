# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:58:36 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:Global and Local Variables
"""
G_VAR = "this is a global variables"
l_var = None
def test_g_var():
    global l_var 
    l_var = "this is a local variables 1"
    print("run test_g_var()")
    return None
print(l_var)

def test_l_var():
    global l_var
    l_var = "this is a local variables 2"
    print("run test_l_var()")
    return None
print(l_var)

test_g_var()
print(l_var)
test_l_var()
print(l_var)
