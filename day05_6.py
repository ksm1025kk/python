# 외부 함수를 사용하는 법 : import
# 모듈 : 부품

# import 모듈명
# import 모듈명 as 별명
# from 모듈명 import 함수명

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font = font_manager.FontProperties(fname = 'H2GTRE.TTF'). get_name()
rc('font', family = font)
lst = [10, 20, 30, 40, 50, 70, 60, 90, 80]

plt.title('분포도') 
plt.xlabel('점수') 
plt.ylabel('갯수') 
plt.hist(lst)                                       # 막대그래프 그려줘
plt.show()                                          # 보여줘