import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

# 常態分佈機率密度函數
x = np.linspace(-3,3,1000)
y = 1/((2*np.pi)**0.5) * np.exp(-x**2 /2)

plt.plot(x,y,color='b')

plt.grid()
plt.show()


# A normal continuous random variable.
# The location (loc) keyword specifies the mean.
# The scale (scale) keyword specifies the standard deviation.

x = np.linspace(-3,3,1000)
plt.plot(x,st.norm.pdf(x,loc=0,scale=1))
plt.plot(x,st.norm.pdf(x,loc=-1,scale=2))
plt.plot(x,st.norm.pdf(x,loc=1,scale=0.5))

plt.grid()
plt.show()



