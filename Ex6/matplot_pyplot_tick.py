# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 14:25:06 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:matplotlib.pyplot tick
"""
import matplotlib.pyplot as plt
import numpy as np

#數據設定
x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
plt.plot(x, y, linewidth=10)
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='r', edgecolor='None', alpha=0.3))
plt.show()

