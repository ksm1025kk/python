# pip install scikit_learn

import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print('사이킷런 버전:',sklearn.__version__)

운동시간 = [[1], [2], [3], [4], [5]]
근육량 = [[0], [1], [2.5], [5], [6.5]]

lin = LinearRegression()
# 인공지능 학습 fit(x,y)
lin.fit(운동시간, 근육량)

근육량예측 = lin.predict(운동시간)
print(근육량)
print('2.5시간 운동하면 근육 증가량은',lin.predict([[2.5]]), '입니다.')

plt.scatter(운동시간, 근육량, color = 'blue')               # 점 (제공데이터)
plt.plot(운동시간, 근육량예측, color = 'green')             # 선 (예측값)
plt.show()




