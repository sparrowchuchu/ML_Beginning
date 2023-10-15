import matplotlib.pyplot as plt
import numpy as np


""" convergence 收斂 """

alcohol = 58
# for x in range(0,11):
#     if x > 0:
#         alcohol *= 0.5
#     print(f"當 x = {x:2d}, 酒精濃度 = {alcohol}") 
x = [x for x in range(0,11)]
y = [alcohol*(1/2)** y for y in x]
plt.axis([0,12,0,60])
plt.plot(x,y)
plt.xlabel("Times")
plt.ylabel("Alcohol concentration")
plt.title("convergence")
plt.grid()
plt.show()


""" divergence 發散 """

# 當x值趨近於0時，y值將趨近於無窮大。
x = np.linspace(1, 0.01, 101)
y = [1/y for y in x]
plt.axis([0,1,0,101])
plt.plot(x,y)
plt.plot(x[100],y[100],'-o')
plt.xlabel("x")
plt.ylabel("y")
plt.title("divergence")
plt.grid()
plt.show()

# 當x值趨近於0時，y值將趨近於負無窮大。
x = np.linspace(-1, -0.01, 101)
y = [1/y for y in x]
plt.axis([-1,1,-101,101])
plt.plot(x,y)
plt.plot(x[100],y[100],'-o')
plt.xlabel("x")
plt.ylabel("y")
plt.title("divergence")
plt.grid()
plt.show()
