# 생성자
class 회사프로그램:
    n1 = 0                  #클래스 안에 있는 변수 == 멤버변수
    n2 = 0
    # 메서드 : 클래스 안에 있는 변수(매개변수 가장 앞에 self라는 매개변수를 만들어놓아야함)
    def AbsSum(self, n1, n2):      # self : 매서드 고정 매개변수로 사용할 때 채우지 않음(사용 x)
        result = 0                # 지역변수 (함수 안에 있는 변수)
        if n1 < 0:
            n1 = n1 * -1
        if n2 < 0:
            n2= n2 * -1
        self.n1 = n1
        self.n2 = n2                    
        result = n1+n2
        return result
def Last(self):
    print(self.n1 + self.n2)
# 생성자 __init__ : 객체화하는 순간에 사용될 매서드
def __init__(self):
    # 생성자
    # 객체화를 하는 순간에 실행될 코드
    # 객체화하는 순간에 클래스면 옆에 있는 ()
    print('회사프로그램 객체화에 성공하였습니다.')
def __init__(self, 수1, 수2):
    self.AbsSum(수1, 수2)

a = 회사프로그램()
b = 회사프로그램()