import matplotlib.pyplot as plt
import numpy as np


""" 定積分簡單的應用。 """

# 原始函數F(x)的係數
a = 1
b = 1

# 繪製此函數積分區間圖形
x = np.linspace(0, 6, 1000)
y = a*x + b
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=1)&(x<=5),
                 facecolor='lightgreen')
plt.grid()
plt.show()


# 原始函數F(x)的係數
a = 1

# 繪製此函數積分區間圖形
x = np.linspace(0, 4, 1000)
y = a*x**2
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=1)&(x<=3),
                 facecolor='lightgreen')
plt.grid()
plt.show()


""" 定積分出現負值的處理。 """
# 原始函數F(x)的係數
a = 1

# 繪製此函數積分區間圖形
x = np.linspace(-3, 3, 1000)
y = a*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=0)&(x<=2),
                 facecolor='lightgreen')
plt.fill_between(x, y1=y, y2=0, where=(x<=0)&(x>=-2),
                 facecolor='lightblue')
plt.grid()
plt.show()






