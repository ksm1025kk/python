# 횟수를 입력받아서 그 수만큼 Hello 출력
# ex) 5 입력시 1번째 Hello ~ 5번째 Hello 출력

# count = int(input('반복할 횟수를 입력하시오. '))
# i = 0
# while i < count : 
#     i += 1
#     print(i,'번째 Hello')

# 1 ~ 100 사이에서 7의 배수만 출력하는 프로그램(while 안에서 if 를 사용)
# i = 1
# while i < 101:
#     if(i % 7) == 0:
#         print(i)
#     i += 1

# 커피 1 잔에 300원, 금액을 입력하여 몇 잔의 커피와 잔돈이 얼마나 남는지 출력
price = 300
금액 = int(input('금액은 얼마인가요? '))
커피잔수 = 0
while 금액 >= price:
    금액 -= price
    커피잔수 += 1
    print('커피',커피잔수,'잔, 잔돈',금액,'원')




        

