import matplotlib.pyplot as plt
import numpy as np


""" 指數是負整數 """

x=np.linspace(-0.01,-5,100)  # 左下角圖
y=[1/y for y in x]
plt.plot(x,y)

x=np.linspace(0.01,5,100)  # 右上角圖
y=[1/y for y in x]
plt.plot(x,y)

plt.axis([-5,5,-5,5])
plt.xticks(range(-5,6,1))
plt.yticks(range(-5,6,1))
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()


