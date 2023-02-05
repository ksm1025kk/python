# 변수와 자료형
# 변수는 저장공간/대입연산자 '='를 통해서 만들고 값을 대입
# 출력 : print(), 입력 : input()
# 자료형 : str(문자열형), int(정수형), float(실수형), list(리스트), dict, set, tuple ...등등
# 자료형 변환 -> int(input())

변수 = '담고자하는 데이터 값'
변수 = '수정하고자 하는 값'
변수 = input('키보드로 입력할 값을 적으세요. ')
print('', 변수, '')

정수 = 0
정수 = -1
정수 = int('-3')
정수 = int(input('숫자만 입력하시오. '))
print('==', 정수, '==')
# 연산자 : 특정 기능을 갖고 있는 기호
# +, -, *, /, %, **, //
# 누적연산자 : 연산 후에 그 값을 다시 대입
# +=, -=, *=, /=, %=
# 관계연산자 : and, or, not
# 비교 연산자 : <, >, <=, >=, !=

num = 5 + 3
num = 2 - 1
num = 3 * 3

num += 3
num -= 1

3 > 2                       # True
3 <= 2                      # False

3 > 2 and 3 <= 2            # and : 양쪽 다 맞아야 True, 나머진 False
3 <= 2 or 3 > 2             # False : 둘 중 하나만 맞아도 True, 다 틀리면 False

# 제어문
# 조건문 : if, elif, else
# 반복문 : while, for
# 기타 제어문 : break, continue

if 정수 < 10:
    print('10보다 작다.')
elif 정수 < 100:
    print('10 ~ 100 사이다')
else:
    print('그 외의 값이다.')

while True:
    print('무한반복중')
    정수 += 1
    if 정수 != 0:
        break               # 반복문 탈출

for index in range (10):
    print('10번 반복중', (index), '번')
    if index % 2 == 0:
        continue                        # 한번 스킵
    print('10번 반복 중', (index +1), '번')

# 함수 : python 언어에서 지원해주는 함수
# 외장함수 : python 에서 제공해주지 않으나 import 로 추가한 함수
# 사용자 정의 함수 : 내가 직접 만드는 연산자 def

# 함수 : 코드를 저장하는 기술 _ 코드 변화 대처에 용이(코드 재활용)
# 외부모듈추가 : import 모듈명
#               impott 모듈명 as 별명
#               from 모듈명 import 모듈일부

lst = ['전역', '변수', '리스트형']
max(lst)                            # 내장함수 사용

def 사용자정의함수():                # 함수 정의 def
    for i in lst:
        print(i, end=', ')

사용자정의함수()                    # 함수 사용

# 클래스 : 변수와 함수를 묶는 기술
# 쉽게 제공하고 가독성을 좋게 하기 위해서
# 멤버변수 : 클래스 안에서 생성한 변수(self. 을 통해서 사용 가능)
# 메서드 : 클래스 안에서 정의된 함수(self를 갖고 있음)

# 객체화를 사용하기 위해선 변수를 담아 사용한다. 이때 변수는 객체라고 부른다.
# 생성자 : 객체화하는 순간에 사용되는 메서드 def __init__(self):
# 상속 : 클래스를 컴퓨터가 복붙, 북붙한 후에 메서드를 추가하거나 재정의

class MyClass:
    멤버변수1 = ''
    멤버변수2 = 0
    def 메서드1(self):
        print('MyClass의 메서드1 사용')
    def 메서드2(self, str1, num1):
        self.멤버변수1 = str1
        self.멤버변수2 = num1
        self.멤버변수3.append(str1)
        self.멤버변수3.append(num1)
    def __init__(self):
        self.메서드1()

객체변수 = MyClass()                        # 객체화 : 클래스는 사용을 위해 변수로 만들어 주어야한다.
객체변수.메서드2('sample', 1)

class MyClassEX(MyClass):                  # 상속 : ()에 있는 클래스를 내 클래스에 복붙한다
    pass
                