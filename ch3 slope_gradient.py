import matplotlib.pyplot as plt
import numpy as np


""" 曲線的斜率其實是切線。 """

# 曲線公式 y = x*x
x=np.linspace(-5,5,101)
y=[y*y for y in x]
plt.axis([-5,5,0,30])
plt.plot(x,y)
plt.xticks(range(-5,6,1))
plt.xlabel("x")
plt.ylabel("y")
plt.title("slope / gradient")
plt.grid()
plt.show()

# 曲線公式 y = x*x
x=np.linspace(-2,2,101)
y=[y*y for y in x]
plt.axis([-2,2,0,4])
plt.plot(x,y)
plt.plot([1,2],[1,4],'-o') # 繪製AB連線
plt.xticks(range(-2,3,1))
plt.text(1-0.15,1+0.1,'A')
plt.text(2-0.15,4-0.15,'B')
plt.xlabel("x")
plt.ylabel("y")
plt.title("slope / gradient")
plt.grid()
plt.show()