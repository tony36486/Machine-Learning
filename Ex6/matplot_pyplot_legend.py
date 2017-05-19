# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:35:21 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:matplotlib.pyplot Legend
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
#set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set new sticks
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# set line syles
l1, = plt.plot(x, y2, label='linear line')
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='square line')

#設定圖利
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')

"""
能單獨使用,而圖利印出為線的預設label
plt.legend(loc='upper right')

"""

