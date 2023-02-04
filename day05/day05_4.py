# + - * /

def 더하기(num1, num2, num3):
    print(num1 + num2 + num3)
def 빼기(num1, num2, num3):    
    print(num1 - num2 - num3)
def 곱하기(num1, num2, num3):   
    print(num1 * num2 * num3)
def 나누기(num1, num2, num3):
    print(num1 / num2 / num3)
    

print(1+2)
더하기(1, 2, 3) 
빼기(3, 2, 1)
곱하기(1, 2, 3)
나누기(10, 2, 2)
print()

def 절대값더하기(a, b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    print(a+b)
절대값더하기(3, 7)              # 10          
절대값더하기(-4, 3)             # 7