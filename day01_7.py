# 연산자 
a = 10
b = 3

a + b                     # 덧셈           13
a - b                     # 뺼셈           7   
a * b                     # 곱셈           30
a / b                     # 나눗셈         3.3 
a % b                     # 나머지 구하기   1
a ** b                    # a의 b제곱     1000

# 비교연산자 :  True OR False
a == b                    # 같다 
a != b                     # 다르다
a > b                     # a 가 b 보다 크다
a < b                     # a 가 b 보다 작다
a >= b                    # a 가 b 보다 크거나 같다
a <= b                    # a 가 b 보다 작거나 같다

# 대입연산자 주의할 점
a = a                     # 왼쪽 a는 공간의 개념, 오른쪽 a는 값

#줄인말
a += b                    # a = a + b
a -= b                    # a = a - b
a *= b                    # a = a * b
a /= b                    # a = a / b

(a + b) * a               # 우선순위

# 관계연산자 and/or/not
print(a > 5 and a < 15) # a는 5보다 크고 15보다 작다. True
print(a > 5 or a < 0)   # b는 5보다 크거나 0보다 작다. True
print(not b==3)         # True 는 False 로 False 는 True 로 바꿈
