# 20세 이상은 성인
# 14세 이상은 청소년
# 14세 미만은 어린이

나이1 = int(input('문제 1 : 나이는 몇 살입니까? '))
if 나이1 >= 20:
    print('성인입니다.')
elif 나이1 >= 14:
    print('청소년입니다.')
else:
    print('어린이입니다.')
print('프로그램을 종료합니다.')
print('')

# 0~7 유치원
# 8~13 초등학교
# 14~16 중학교
# 17~19 고등학교
# 20~22 대학교
# 23~ 회사원
# 0미만 잘못 입력함

나이2 = int(input('문제 2 : 나이는 몇 살입니까? '))
if 나이2 <= 0:
    print('잘못 입력함')
elif 나이2 < 8:
    print('유치원')
elif 나이2 < 12:
    print('초등학교')
elif 나이2 < 16:
    print('중학교')
elif 나이2 < 19:
    print('고등학교')
elif 나이2 < 22:
    print('대학교')
else:
    print('회사원')
print('프로그램을 종료합니다.')
print('')




