# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 21:28:50 2017
python 3.6ver
@author: tony

this code is a exercise of ML class
exercise:matplotlib.pyplot
"""
import matplotlib.pyplot as plt
import numpy as np
#定義 x 為 介於 -1~1 之間 平均分布的50個點
x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = x**2
#定義視窗
plt.figure()
#繪製圖形
plt.plot(x,y1)
#定義視窗
plt.figure()
#繪製圖形
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
#繪製圖形
plt.plot(x,y2)
#設置x軸範圍
plt.xlim((-1, 2))
#設置y軸範圍
plt.ylim((-2, 3))
#設置x軸標籤
plt.xlabel('I am x')
#設置y軸標籤
plt.ylabel('I am y')
#設定X軸間隔
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
#設定y軸間隔
plt.yticks([-2, -1.8, -1, 1.22, 3],
           ['really bad', 'bad', 'normal', 'good', 'really good'])
"""
變更為數學字體 [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$']
"""
#獲取目前座標軸訊息
ax = plt.gca()
#設定邊框
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#設定x軸
#ax.xaxis.set_ticks_position('bottom')
#設定y軸原點
ax.spines['bottom'].set_position(('data', 0))
#設定x軸原點
ax.spines['left'].set_position(('data',0))
#顯示圖形
plt.show()

