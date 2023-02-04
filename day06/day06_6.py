# 300명이 방문하였을 때 판매량을 예측하세요

# 머신러닝 모듈
import sklearn
# 그래프 모듈
import matplotlib.pyplot as plt
# 수학/과학 계산 모듈
import numpy as np
# 다차원 데이터 모듈
import pandas as pd
from sklearn.linear_model import LinearRegression

origindata = pd.read_csv('kyobo.csv', encoding='cp949')
print(origindata.head())

X = origindata.iloc[:,:-1].values
y = origindata.iloc[:,-1].values

print(X)
print(y)

machinerunning = LinearRegression()
machinerunning.fit(X, y)
y_pred = machinerunning.predict(X)
print('예측한 y 값:\n',y_pred)

print('AI예측값:', machinerunning.predict([[200]]))

plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.title('kyobo selling')
plt.xlabel('visit')
plt.ylabel('sell')
plt.show()