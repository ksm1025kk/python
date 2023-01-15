# 튜플 tuple
# tuple = ()
# 튜플 : 추가할 수 없음

manu = ('돈까스','순두부','김밥')           # 추가x
print(manu[0])
print(manu[1])
print(manu[2])

name1 = ''
name2 = ''
name3 = ''

name1, name2, name3 = manu
name1, name2, name3 = ('안녕하세요','hello','반갑습니다')
print(name1, name2, name3)

for i in manu:
    print(i)