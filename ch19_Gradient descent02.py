import matplotlib.pyplot as plt
import numpy as np
import time

""" 
Gradient descent 梯度下降法

請輸入學習率和最初值，這個程式將以梯度下降法繪製與
找出函數L的最小值，這個迴圈基本上會執行15次。 
"""

# 誤差函數  L = 7*t**2 - 1120*t + 45850
# 其微分結果 L'= 14*old_x-1120

def myfun(t):
    return (7*t**2 - 1120*t + 45850)

rate=eval(input('請輸入學習率: '))
init_x=eval(input('請輸入參數值: ')) # 初始值

x=np.arange(0,200,0.1)
y=myfun(x)
plt.plot(x,y)                   # 繪製函數

plt.xlabel('x')
plt.ylabel('L')                 # 誤差
plt.title(f'rate={rate}   initial={init_x}')

new_x=0
# old_x=0
for i in range(1,16):           # 15圈
    if i ==1:
        old_x=init_x
    else:
        old_x=new_x
    slope=14*old_x-1120         # 斜率
    new_x=old_x-rate*slope      # 計算新的參數
    
    plt.plot([old_x,new_x],[myfun(old_x),myfun(new_x)],'go-')  # color='green', marker='o', linestyle='dashed'
    print(f'loop = {i:2d}, old_x = {old_x:4.2f}, new_x = {new_x:4.2f}')
    time.sleep(1)

plt.grid()
plt.show()



