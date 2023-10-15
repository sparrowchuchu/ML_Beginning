import matplotlib.pyplot as plt
import numpy as np


""" 最大概似估計法 與 多元回歸分析 """
# 使用 多元回歸分析 找出 最小誤差平方和
# 可得到 最大概似估計值

t = [85, 91, 76, 102, 68, 72, 66]   # 定義 預估裝潢天數
ave = np.mean(t)                    # 平均天數
x = np.linspace(0, 200, 200)        # 陣列 x 
y = np.linspace(0, 200, 200)        # 陣列 y
min_x = 100                         # 預估 x的最初預估極值
min_y = 100                         # 預估 y的最初預估極值

for i in range(len(x)):
    sum_ss = 0
    # sum_ss = (ave - x[i]) ** 2 # 
    for j in range(len(t)):
        sum_ss += (ave - x[i]) ** 2 # 計算 誤差值平方和
    y[i] = sum_ss
    if y[i] < min_y:                # 比較是否為最小誤差平方和
        min_x = i
        min_y = y[i]
        
plt.plot(x,y)
plt.plot(min_x, min_y, '-o')
plt.text(min_x-20, min_y+2000, '('+str(round(min_x, 1))+
         ', '+str(round(min_y, 5))+')')





