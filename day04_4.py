# 문자열을 저장하는 리스트
lst = []
flag = 0
# 사용자에게 입력을 받아 리스트를 구성
# 1 : 추가하기, 2 : 수정하기, 3 : 삭제하기, 4 : 전체보기

while True:
    num = int(input('1 : 추가, 2 : 수정, 3 : 삭제, 4 : 조회, 0 : 종료, 번호를 선택하세요 : ')) 
    if num == 1:
        lst.append(input('추가할 값을 입력하세요 ==> '))                    # 뒤에 추가됨
                    # 추가할 값을 입력
    elif num == 2:
        origin = input('수정할 값을 입력하세요 ==> ')
        for i in lst:
            if i == origin:
                flag = 1                                               # 입력된 값이 없다면 
        
        if flag == 1:
            flag = 0
            result = lst.index(origin)            # 수정할 값의 위치를 찾음            
        else:
            print('없음')
            continue
        #     result = lst.index(input('잘못된 값입니다. 다시 입력하세요 ==> '))
        lst[result] = (input('수정할 값을 입력하세요 ==> '))                # 찾은 위치의 값을 입력받은 값으로 수정
                    # 값을 수정
    elif num == 3:                                                        # 입력받은 값을 제거
        lst.remove(input('삭제할 값을 입력하세요 ==> '))
        # if lst.remove(input('삭제할 값을 입력하세요 ==> ')) != lst:         # 입력된 값이 없다면    
        #     lst.remove(input('잘못된 값입니다. 다시 입력하세요 ==> '))
                           # 삭제할 값 입력
    elif num == 4:                                                        
        for i in lst:
            print(i)       # 전체 조회     
    elif num == 0:                                                        # 프로그램을 종료
        print('프로그램 종료')
        break
    else:
        print('없는 번호입니다.')
