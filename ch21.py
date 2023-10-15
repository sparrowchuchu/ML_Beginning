import numpy as np

'''
將'是否回購'表單問卷轉為'Sigmoid'非線性數學模型。
y = f(x) = 1/1+e^-x
y:是否回購 0或1。

Pi = 1/1+e^-xiβ
y(Pi):因變數, 回購虛擬變數(回購機率)。
x:自變數; x0:截距, x1:台北市虛擬變數, x2:客訴虛擬變數。
beta:迴歸係數。

用梯度下降法求 - 最大beta0概似值。
'對數概似函數'是用來計算'最大值';
'梯度下降法'是計算'最小'損失值;
所以將'對數概似函數'乘以'-1'，求'梯度下降法'最小值。
C(beta) = -ln L(beta)

 lim  = f(x+dx) - f(x)
dx->0        dx

x1 = f(x+dx)
x2 = f(x)
delta_x = x的極小變量
'''
def f1():
    ''' 1-54 '''
    x1=beta[0]+delta_x+np.log(1+np.exp(-(beta[0]+delta_x)))
    x2=beta[0]+np.log(1+np.exp(-beta[0]))
    # 人數 * f(beta)對beta[0]偏微分。 用梯度下降法求 最大beta0概似值
    beta0=people[0] * (x1-x2)/delta_x
    cur_beta[0]+=beta0

def f2():
    ''' 55-90 '''
    x1=np.log(1+np.exp(-(beta[0]+delta_x)))
    x2=+np.log(1+np.exp(-beta[0]))          
    beta0=people[1]*(x1-x2)/delta_x
    cur_beta[0]+=beta0   

def f3():
    ''' 91-108 '''
    x1 = beta[0]+delta_x+beta[2] \
         +np.log(1+np.exp(-(beta[0]+delta_x+beta[2])))
    x2=beta[0]+beta[2]+np.log(1+np.exp(-(beta[0]+beta[2])))
    beta0=people[2]*(x1-x2)/delta_x
    cur_beta[0]+=beta0   
    beta2=beta0
    cur_beta[2]+=beta2

def f4():
    ''' 109-120 '''
    x1=np.log(1+np.exp(-(beta[0]+delta_x+beta[2])))
    x2=np.log(1+np.exp(-(beta[0]+beta[2])))
    beta0=people[3]*(x1-x2)/delta_x
    cur_beta[0]+=beta0 
    beta2=beta0
    cur_beta[2]+=beta2

def f5():
    ''' 121-184 '''
    x1 = beta[0]+delta_x+beta[1] \
         +np.log(1+np.exp(-(beta[0]+delta_x+beta[1])))
    x2=beta[0]+beta[1]+np.log(1+np.exp(-(beta[0]+beta[1])))
    beta0=people[4]*(x1-x2)/delta_x
    cur_beta[0]+=beta0 
    beta1=beta0
    cur_beta[1]+=beta1 

def f6():
    ''' 185-280 '''
    x1=np.log(1+np.exp(-(beta[0]+delta_x+beta[1])))
    x2=np.log(1+np.exp(-(beta[0]+beta[1])))
    beta0=people[5]*(x1-x2)/delta_x
    cur_beta[0]+=beta0 
    beta1=beta0
    cur_beta[1]+=beta1

def f7():
    ''' 185-288 '''
    x1 = beta[0]+delta_x+beta[1]+beta[2] \
         +np.log(1+np.exp(-(beta[0]+delta_x+beta[1]+beta[2])))
    x2 = beta[0]+beta[1]+beta[2] \
         +np.log(1+np.exp(-(beta[0]+beta[1]+beta[2])))
    beta0=people[6]*(x1-x2)/delta_x
    cur_beta[0]+=beta0 
    beta1=beta0
    cur_beta[1]+=beta1
    beta2=beta0
    cur_beta[2]+=beta2
    
def f8():
    ''' 289-300 '''
    x1=np.log(1+np.exp(-(beta[0]+delta_x+beta[1]+beta[2])))
    x2=np.log(1+np.exp(-(beta[0]+beta[1]+beta[2])))
    beta0=people[7]*(x1-x2)/delta_x
    cur_beta[0]+=beta0 
    beta1=beta0
    cur_beta[1]+=beta1
    beta2=beta0
    cur_beta[2]+=beta2


delta_x=0.00001 
rate=0.003                       # 學習率
people=[54,36,18,12,64,96,8,12]  # 各階段人數
beta=[1,1,1]                     # 初值

for i in range(500):
    cur_beta=[0,0,0]
    f1()
    f2()
    f3()
    f4()
    f5()
    f6()
    f7()
    f8()
    cur_beta[0]=beta[0]-cur_beta[0]*rate
    cur_beta[1]=beta[1]-cur_beta[1]*rate
    cur_beta[2]=beta[2]-cur_beta[2]*rate
    beta=cur_beta
    print(beta)                # 迴歸係數的收斂過程
    
print(f'迴歸係數 {beta[0]:6.5f}, {beta[1]:6.5f}, {beta[2]:6.5f}')   
print(f'>截距         {beta[0]:6.5f},\n>台北市虛擬變數 {beta[1]:6.5f},\n>客訴虛擬變數   {beta[2]:6.5f}')
                
# 台北市1, 外縣市0
x1=np.exp(beta[1]*1)
x2=np.exp(beta[1]*0) 
odds_ratio=x1/x2
print(f'台北市與外縣市勝算比 = {odds_ratio:6.4f}') 








