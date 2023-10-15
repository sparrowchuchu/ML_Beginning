import matplotlib.pyplot as plt
import numpy as np


""" 用切線繪製二次函數。 """

# y = f(x) = 3x** - 12x + 10 
a = 3
b = -12
c = 10

# 繪製此函數圖形
x = np.linspace(0,4,50)
y = a*x**2 + b*x + c
plt.plot(x, y, color='b')

# 繪製經過 x = 0, 1, 2, 3, 4 的切線。
for counter in range(0,41):
    x_loc = counter / 10
    y_loc = a*x_loc**2 + b*x_loc + c  # y座標
    slope = 6 * x_loc - 12            # 每一點的斜率
# x_new和y_new是經過切線的座標，只取3點連線。
    x_new = [x_loc-1, x_loc, x_loc+1]
    y_new = [slope * (x - x_loc) + y_loc for x in x_new]
    plt.plot(x_new, y_new, color='g')
plt.grid()
# plt.axis('equal')    # 不調整圖形比例
plt.show()


