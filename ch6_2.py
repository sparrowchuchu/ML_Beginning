from scipy.optimize import root
import matplotlib.pyplot as plt
import numpy as np


""" 計算兩個線性方程式的交叉點。 """

# f(x) = x**2 - 5x + 7
# f(x) = 2x + 1

def fx(x):
    return (x**2-5*x+7)

def fy(x):
    return (2*x+1)

# 計算交叉點
r1 = root(lambda x:fx(x)-fy(x),0)  # 初始迭代值0
r2 = root(lambda x:fx(x)-fy(x),5)  # 初始迭代值5
print('x1 = %4.2f, y1 = %4.2f' % (r1.x,fx(r1.x)))
print('x2 = %4.2f, y2 = %4.2f' % (r2.x,fx(r2.x)))

# 繪製fx函數圖形
x1 = np.linspace(0,10,40)
y1 = fx(x1)
plt.plot(x1,y1,'-',label='x**2 - 5x + 7')

# 繪製fy函數圖形
x2 = np.linspace(0,10,40)
y2 = fy(x2)
plt.plot(x2,y2,'-',label='2x + 1')

# 繪製交叉點
plt.plot(r1.x,fx(r1.x),'o')
plt.plot(r2.x,fx(r2.x),'o')

plt.legend(loc='best')
plt.show()





