# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 19:42:51 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:copy & deepcopy 
"""
import copy
a = [1, 2, 3, [4, 5]]
b = a
print(id(a) == id(b))
print(id(a[0]) == id(b[0]))
print(id(a[1]) == id(b[1]))
print(id(a[2]) == id(b[2]))
print(id(a[3][0]) == id(b[3][0]))
print(id(a[3][1]) == id(b[3][1]))

c = copy.copy(a)
print("try copy")
print(id(a) == id(c))
print(id(a[0]) == id(c[0]))
print(id(a[1]) == id(c[1]))
print(id(a[2]) == id(c[2]))
print(id(a[3][0]) == id(c[3][0]))
print(id(a[3][1]) == id(c[3][1]))

d = copy.deepcopy(a)
print("try deepcopy")
print(id(a) == id(d))
print(id(a[0]) == id(d[0]))
print(id(a[1]) == id(d[1]))
print(id(a[2]) == id(d[2]))
print(id(a[3][0]) == id(d[3][0]))
print(id(a[3][1]) == id(d[3][1]))

print()

a[2] = 4
a[3][0] = 3
print("after change 'a' by a[n] = x")
print('a:', a,
      'b:', b,
      'c:', c,
      'd:', d)

a = [1, 2, 4, [3, 5]]
print("after change 'a' by a[s, s, d, [d , s]]")
print('a:', a,
      'b:', b,
      'c:', c,
      'd:', d)

print("try copy")
print(id(a) == id(c))
print(id(a[0]) == id(c[0]))
print(id(a[1]) == id(c[1]))
print(id(a[2]) == id(c[2]))
print(id(a[3][0]) == id(c[3][0]))
print(id(a[3][1]) == id(c[3][1]))

print("try deepcopy")
print(id(a) == id(d))
print(id(a[0]) == id(d[0]))
print(id(a[1]) == id(d[1]))
print(id(a[2]) == id(d[2]))
print(id(a[3][0]) == id(d[3][0]))
print(id(a[3][1]) == id(d[3][1]))