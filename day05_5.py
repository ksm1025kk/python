# 문제1
def 총합(lst):
    result = 0
    for i in lst:
        result += i
    return result

lst = [10, 20 ,30, 40 ,50]
sum = 총합(lst)
avg = sum/len(lst) 

print('총합은', sum)
print('평균은', avg)
print()
# 문제 2 : 입력한 갯수만큼 *을 표시하는 함수
def star(num):
    result = ''
    for i in range(num):
        result += '*'
    return result

s1 = star(3)
s2 = star(5)
print(s1)
print(s2)