import numpy as np
import matplotlib.pyplot as plt


d_x=np.linspace(1.0,5.0,21)
d_y=[4,4,5,6,8,12,18,22,35,40,45,
     33,28,30,32,36,38,41,35,31,20]
d_y=[data/100 for data in d_y]

plt.rcParams['font.family']=['Microsoft JhengHei']  # 微軟正黑體
plt.scatter(d_x,d_y,color='green')

x=np.linspace(1.0,5.0,1000)
y=np.linspace(1.0,5.0,1000)

for i in range(len(x)):
    f1=1/(1+np.exp(-0.828*x[i]+4.006))
    f2=1/(1+np.exp(6.504*x[i]-33.212))
    f3=1/(1+np.exp(-9.19*x[i]+22.976))
    f4=1/(1+np.exp(22.976*x[i]-73.522))
    y[i]=f1+f2-1+0.3*(f3+f4-1)
    
plt.plot(x,y)
plt.title('蘋果銷售調查')
plt.xlabel('蘋果品質 Quality',fontsize=14)
plt.ylabel('銷售率 Rate',fontsize=14)
plt.grid()
plt.show()



# 使用線性函數擬合數據
x=np.linspace(1.0,5.0,21)
y=[4,4,5,6,8,12,18,22,35,40,45,
      33,28,30,32,36,38,41,35,31,20]

plt.scatter(x,y,color='green')

coef=np.polyfit(x,y,6)     # 回歸直線係數
model=np.poly1d(coef)      # 線性回歸方程式
reg=np.linspace(1,5.0,100)

plt.title('蘋果銷售調查')
plt.xlabel('蘋果品質 Quality',fontsize=14)
plt.ylabel('銷售率 Rate',fontsize=14)
plt.plot(reg,model(reg),color='red',label='回歸直線係數6')
plt.legend(loc='upper left')
plt.grid()
plt.show()





