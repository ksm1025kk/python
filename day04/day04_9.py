# set 세트 = {'','', ''}
# 중복이 x 
# 중복된 값을 추가하려하면 무시
s = ({})
s2 = {'a','c','e'}

# 추가 : add
s.add('a')
s.add('b')
s.add('a')
s.add('c')
s.add('d')
# 빼기 remove
s.remove('d')

print(s)
print(s2)

# 교집합
s_kyo = s & s2
print(s_kyo)
# 합집합
s_hap = s | s2
print(s_hap)
# 차집합
s_cha = s - s2