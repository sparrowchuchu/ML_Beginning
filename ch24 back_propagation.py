

rate=0.1                 # 學習率
w=[0,1,1,1,1,1,1]        # weight,索引0沒有作用。
new_w=[0,0,0,0,0,0,0]    # new weight,索引0沒有作用。
x=[0,1,0.5]              # x,索引0沒有作用。
v=4.5                    # 目標值

u1=w[1]*x[1]+w[2]*x[2]
print(f'  u1   = : {u1:5.3f}')
u2=w[3]*x[1]+w[4]*x[2]
print(f'  u2   = : {u2:5.3f}')
y=w[5]*u1+w[6]*u2
print(f'   y   = : {y:5.3f}')
E=0.5*(y-v)**2
print(f'   E   = : {E:5.3f}')
dEdy=y-v
print(f'y - v  = : {dEdy:5.3f}')
dydw5=u1
print(f'dedw5  = : {dydw5:5.3f}')
dEdw5=dEdy*dydw5
print(f'dEdw5  = : {dEdw5:5.3f}')
new_w[5]=w[5]-rate*dEdw5
print(f'new_w5 = : {new_w[5]:5.3f}')
dydw6=u2
dEdw6=dEdy*dydw6
print(f'dEdw6  = : {dEdw6:5.3f}')
new_w[6]=w[6]-rate*dEdw6
print(f'new_w6 = : {new_w[6]:5.3f}')
dEdw1=(y-v)*w[5]*x[1]
new_w[1]=w[1]-rate*dEdw1
print(f'new_w1 = : {new_w[1]:5.3f}')
dEdw2=(y-v)*w[5]*x[2]
new_w[2]=w[2]-rate*dEdw2
print(f'new_w2 = : {new_w[2]:5.3f}')
dEdw3=(y-v)*w[6]*x[1]
new_w[3]=w[3]-rate*dEdw3
print(f'new_w3 = : {new_w[3]:5.3f}')
dEdw4=(y-v)*w[6]*x[2]
new_w[4]=w[4]-rate*dEdw4
print(f'new_w4 = : {new_w[4]:5.3f}')








