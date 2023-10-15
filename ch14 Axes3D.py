import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# 
def f(x,y):              # 曲面函數
    return (1-(x**0.5)/2 - (y**0.5)/2)

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(0,1,0.01)  # 曲面 X 區間
Y = np.arange(0,1,0.01)  # 曲面 Y 區間
X,Y = np.meshgrid(X,Y)   # 建立取樣數據
ax.plot_surface(X, Y, f(X,Y), color='lightgreen', 
                alpha=0.6)  # 繪製3D圖

plt.grid()
plt.show()


# 
def f(x,y):              # 曲面函數
    return (np.power(x,2) + np.power(y,2))

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-3,3,0.01)  # 曲面 X 區間
Y = np.arange(-3,3,0.01)  # 曲面 Y 區間
X,Y = np.meshgrid(X,Y)   # 建立取樣數據
ax.plot_surface(X, Y, f(X,Y), cmap='hsv', alpha=1)  # 繪製3D圖
ax.set_xlabel('x',color='b')
ax.set_ylabel('y',color='b')
ax.set_zlabel('z',color='b')

plt.grid()
plt.show()


# 
def f(x,y):              # 曲面函數
    r = np.sqrt(np.power(x,2) + np.power(y,2))
    return (np.sin(r))

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-3,3,0.01)  # 曲面 X 區間
Y = np.arange(-3,3,0.01)  # 曲面 Y 區間
X,Y = np.meshgrid(X,Y)   # 建立取樣數據
ax.plot_surface(X, Y, f(X,Y), cmap='rainbow', alpha=1)  # 繪製3D圖
ax.set_xlabel('x',color='b')
ax.set_ylabel('y',color='b')
ax.set_zlabel('z',color='b')

plt.grid()
plt.show()
























