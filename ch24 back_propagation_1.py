

rate=0.1                 # 學習率
w=[0,1,1,1,1,1,1]        # weight,索引0沒有作用。
new_w=[0,0,0,0,0,0,0]    # new weight,索引0沒有作用。
x=[0,1,0.5]              # x,索引0沒有作用。
v=4.5                    # 目標值

while True:
    u1=w[1]*x[1]+w[2]*x[2]
    u2=w[3]*x[1]+w[4]*x[2]
    y=w[5]*u1+w[6]*u2
    print(f'   y   = : {y:5.3f}')
    
    E=0.5*(y-v)**2
    dEdy=y-v
    if abs(dEdy)<0.001:
        break
    dydw5=u1
    dEdw5=dEdy*dydw5
    new_w[5]=w[5]-rate*dEdw5
    
    dydw6=u2
    dEdw6=dEdy*dydw6
    new_w[6]=w[6]-rate*dEdw6
    
    dEdw1=(y-v)*w[5]*x[1]
    new_w[1]=w[1]-rate*dEdw1
    dEdw2=(y-v)*w[5]*x[2]
    new_w[2]=w[2]-rate*dEdw2
    dEdw3=(y-v)*w[6]*x[1]
    new_w[3]=w[3]-rate*dEdw3
    dEdw4=(y-v)*w[6]*x[2]
    new_w[4]=w[4]-rate*dEdw4
    w=new_w

print(w)







