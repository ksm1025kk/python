# 내장 함수 : 파이썬 내장함수(파이썬 언어에서 제공하는 기능)

# eval() : 문자열 형태의 연산식을 숫자로 계산
# result = eval('5+5')
# print('5+5')
# print(result)

# # format() : 문자열로 변환
# result = format(10000)
# # type() : 변수의 자료 형태를 알려줌                    
# print(type(result))                                   # 문자 => <class 'str'>      
# print(type(123))                                      # 숫자 => <class 'int'>  

# # str()
# # int()
# # float()
# # list(), tuple(), set(), dict() : 형변환
# lst = [1, 2, 3]
# print(lst)
# print(tuple(lst))

# result = format(1000000, ',')                        # 천단위마다 ','
# print(result)

# # max() : 리스트중 최대값
# result = max(lst)
# print(result)
# # min() : 리스트중 최소값
# result = min(lst)
# print(result)
# # sum() : 리스트 전체 합계
# result = sum(lst)
# print(result)
# # len() : 리스트에 저장된 갯수
# result = len(lst)
# print(result)
# # abs() : 절대값
# result = abs(-4)
# print(result)
# # pow() : 제곱승
# # 10^3 (10의 3승)
# result = pow(10, 3)
# print(result)
# # divmod() : tuple(몫, 나머지)
# result = divmod(10, 3)
# print(result)
# # round() : 반올림
# result = round(3.141592, 2)
# print(result)
# result = round(3.555555)
# print(result)

# # enumerate() : 반복문이랑 같이 사용됨
# hello = ['h', 'e', 'l', 'l', 'o']
# for item in enumerate(hello):
#     print(item)

# 문제1 : pow 함수를 만들어보자
def 포우(num1, num2):
    result = 1
    for i in range(num2):
        result = result * num1
    return result

result = 포우(10, 3)
print(result)
result = 포우(-2, 3)
print(result)
result = 포우(3, 2)
print(result)

# range(n)          : 0 ~ n-1 까지 반복 (n 번 반복)
# range(n, m)       : n ~ m-1 까지 반복 (m-n 번 반복)
# range(n, m, x)    : n ~ m-1 까지 반복하되, 간격을 x 만큼 뛰면서 (기본값 1)
for i in range(3):
    print('3번 반복', i)

for i in range(1, 3):
    print('3-1번 반복', i)

for i in range(1, 10, 2):
    print(i)

# sorted() : 리스트를 오름차순으로 정렬
lst = [3, 4, 1, 2, 7, 6, 9]
lst2 = sorted(lst)
print(lst2)

# 내림차순 정렬
lst3 = sorted(lst, reverse=True)
print(lst3)