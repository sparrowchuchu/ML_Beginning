import numpy as np


x = np.array([[1,2,3],[4,5,6]])
print(type(x))
print(x)
print('-'*20)


x=np.arange(8).reshape(4,2)
print(x)

y = x.T  # y=x.transpose() 跟 y=x.T 執行結果一樣。
print(y)
print('-'*20)


x = np.array([[1,0,2],[-1,3,1]])
y = np.array([[3,1],[2,1],[1,0]])
z = x@y        # 使用 @ 運算子執行矩陣乘法運算。
print(z)
print('-'*20)


A = np.matrix([[2, 3],
               [5, 7]])
A_inv = np.linalg.inv(A)  # 反矩陣 np.linalg.inv()
print('A_inv = {}'.format(A_inv))
print('E     = {}'.format((A*A_inv).astype(np.int64)))
print('-'*20)


X = np.array([[1,1],[1,2],[1,3]])
XT = X.transpose()
XTX = XT @ X
XTX_inv = np.linalg.inv(XTX)
y = np.array([[5],[10],[20]])
B = XTX_inv @ XT @ y

print(f'a = {B[1][0]}')
print(f'b = {[0][0]}')