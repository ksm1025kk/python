# 반복문  (while, for)
# for를 사용해서 Hello 3번하기

# for 임시변수 in range(3):
#     print('Hello')

# # 임시변수 : while에서 i를 값으로 사용 ==> 임시변수
# i = 0
# while i < 3:
#     print(i, '번째 Hello')
#     i += 1

# for j in range(3):                  # range(3) == range(0, 3) ==> (0 ~ 2)
#     print(j, '번째 Hello')

# i = 1
# for i in range(1, 4):              
#     print(i, '번째 Hello')          # range(1, 4) ==> 0 < 범위 < 4 (1 ~ 3)

# 1 ~ 12월 출력(for)
# for k in range(1, 13):
#     print(k ,'월')

# for k in range(12):
#     print(k+1 ,'월')

# for i in range(7, 101, 7):
#     print(i)

# for g in range(1, 11, 2):
#     print(g+1)

# # for문을 사용하여 54321 출력
# for i in range(5, 10):
#     print(10-i)
# # -------------------------
# num = 5
# for i in range(5):
#     print(num)
#     num -= 1
# # -------------------------
# for i in range(5, 0, -1):
#     print(i)
# # -------------------------


# 양의 정수 1개를 입력받아서 1부터 입력한 숫자까지 합계를 알려주는 프로그램\
# H = int(input('양의 정수를 입력하세요.'))    # 10 
# sum = 0                                    # sum 변수 생성
# for i in range(1, H+1):                    # 1~10 
#     sum += i                               # sum 공간에 i 값을 누적시킴
# print(sum)




num1 = 1
num2 = 2
backup = 0
backup = num1
num1 = num2
num2 = backup
print(num1, num2)
