import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


""" 了解偏微分。 """

# f(x,y) = 2x + 3y
# z = f(x,y) = 2x + 3y
def f(x,y):                       # 3維函數
    return (2*x + 3*y)

fig = plt.figure()
ax = Axes3D(fig)

# 繪製f函數圖形
x = np.arange(0,1,0.01)        # 曲面的 x 區間
y = np.arange(0,1,0.01)        # 曲面的 y 區間
x,y = np.meshgrid(x,y)         # 建立 x, y 數據
z = f(x,y)
ax.plot_surface(x, y, z, color='lightgreen', alpha=1)   # 繪製3D圖

# z 對 x 偏微分 ( x以外的變數視為無關常數。 )
# pz = 2px
def pzx(x):                       # 2維函數
    return (2*x)
x = np.arange(0,1,0.01)
zx=pzx(x)
ax.plot(x, zx, zs=0。, zdir='y', label='pz = 2px')

# z 對 y 偏微分 ( y以外的變數視為無關常數 )
# pz = 3py
def pzy(y):                       # 2維函數
    return (3*y)
y = np.arange(0,1,0.01)
zy=pzy(y)
ax.plot(y, zy, zs=0, zdir='x', label='pz = 3py')

ax.legend()
ax.set_xlabel('X', color='gray')
ax.set_ylabel('Y', color='gray')
ax.set_zlabel('Z', color='gray')
plt.grid()
plt.show()





