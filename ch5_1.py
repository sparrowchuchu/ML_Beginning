import matplotlib.pyplot as plt
import numpy as np


""" 體會二次函數與斜率的關係。 """

# y = f(x) = 3x** - 12x + 10 
a = 3
b = -12
c = 10

# 計算微分 (斜率)
x_min = 12/6

# 將x_min帶入二次函數
y_min = a*x_min**2 + b*x_min + c
plt.text(x_min-0.25, y_min+0.5, '('+str(x_min)+','+str(y_min)+')')
plt.plot(x_min, y_min, '-o', color='r')
print(f'極小值 x 座標 = {x_min}')
print(f'極小值 y 座標 = {y_min}')

# 繪製此函數圖形
x = np.linspace(0,4,50)
y = a*x**2 + b*x + c
plt.plot(x, y, color='b')

# # 繪製極小值的切線
# x_tangent = np.linspace(0, 4, 50)
# y_tangent = [y_min for element in x_tangent]
# plt.plot(x_tangent, y_tangent, color='g')

# 導數
a_de = 6
b_de = -12
x_de = np.linspace(0,4,50)
y_de = a_de*x + b_de
plt.plot(x_de, y_de, color='g')

# 導數為0的(x,y)座標 
x_zero = 12/6
y_zero = 0.0
plt.text(x_zero-0.25, y_zero+1.2, '('+str(x_zero)+','+str(y_zero)+')')
plt.plot(x_zero, y_zero, '-o', color='r')

plt.grid()
plt.show()