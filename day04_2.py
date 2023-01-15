# 리스트 = []   : 변수를 뭉쳐놓은 것

리스트 = [1, 2, 3, 4]
print(리스트)

for i in 리스트:
    print(i)

# 리스트에 저장된 값들 중 하나만 사용하고자 하면
print(리스트[2])

# 3이 저장되어있는 방번호를 찾기
result  = 리스트.index(3)                               # index : 찾기
print('해당 데이터가 저장되어 있는 위치는 : ', result)
리스트.append(314)                                      # append : (뒤에)추가
print(리스트)

리스트.insert(2, 2222)                                  # insert : (중간에)삽입(나머지는 뒤로 밀어버림)
print(리스트)

리스트.remove(2222)                                     #  remove : 제거
print(리스트)

뽑기결과 = 리스트.pop()                                  #  pop : 뒤쪽부터 뽑기
print(리스트)
print(뽑기결과)                                     

리스트.clear()                                          #  clear : 리스트 비우기
print(리스트)

리스트.extend(1,2,3,4,5,6,7,8,9,10)                     #  extend : 리스트 합치기
print(리스트)

리스트.reverse()                                        #  reverse : 리스트 뒤집기
print(리스트)

십의개수 = 리스트.count(10)                              #  count : 리스트 세기
전체개수 = len(리스트)
print(십의개수)                                         #  len : 개수
print('저장된 데이터의 개수는 : ', 전체개수)

리스트.sort()                                           # sort : 오름차순(낮은 순)으로 정렬
print(리스트)

test_리스트 = 리스트.copy()                             # copy : 기존 리스트를 보존하면서 복붙을 만듬
print(test_리스트)
 