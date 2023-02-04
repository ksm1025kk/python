# 머신러닝 모듈
import sklearn
# 그래프 모듈
import matplotlib.pyplot as plt
# 수학/과학 계산 모듈
import numpy as np
# 다차원 데이터 모듈
import pandas as pd
from sklearn.linear_model import LinearRegression
print(sklearn.__version__)

'''
머신러닝 : 데이터(정제)->기계학습->예측결과->머신러닝별 비교 후 선정 
'''
# 데이터를 가져온다
원본데이터 = pd.read_csv('sample.csv', encoding='cp949')
print(원본데이터.head())                                    # .head : 상위 5개만 보기

# X(원인), Y(결과)
X = 원본데이터.iloc[:,:-1].values                                 # [:,:-1]처음부터 마지막 까지
Y = 원본데이터.iloc[:,-1].values

print(X)
print(Y)

선형기계학습 = LinearRegression()
# fit을 사용하면 기계학습을 한다(모델 생성)
선형기계학습.fit(X, Y)
# predict 학습한 내용을 바탕으로 예측을 해
Y_pred = 선형기계학습.predict(X)
print('예측한 y 값:\n',Y_pred)

print('AI예측값:', 선형기계학습.predict([[4.5]]))
print('AI예측값:', 선형기계학습.predict([[6.5],[15]]))

plt.scatter(X, Y, color='green')
plt.plot(X, Y_pred, color='red')
plt.title('corrsion rate/hours')
plt.xlabel('hours')
plt.ylabel('corrsion rate')
plt.show()













