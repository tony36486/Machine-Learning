# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 14:55:53 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:matplotlib.pyplot sctter
"""
import matplotlib.pyplot as plt
import numpy as np
#製作數據
n = 1024    # data size
X = np.random.normal(0, 1, n) # 每個點的X值
Y = np.random.normal(0, 1, n) # 每個點的X值
T = np.arctan2(Y,X) # for color value

#繪製圖型
plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())  # ignore xticks
plt.ylim(-1.5, 1.5)
plt.yticks(())  # ignore yticks

plt.show()

