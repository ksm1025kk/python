# csv파일(구엑셀)
# import : 외장모듈(함수나 클래스)
import csv
def csv파일생성():
    f = open('kyobo.csv', 'w', newline = '')
    wr = csv.writer(f)
    wr.writerow(['방문자수', '판매량'])
    # wr.writerows([[0, '년도', '인구'],[1, '년도', '인구']])
    f.close()

def csv파일이어쓰기():
    f = open('sample.scv', 'a', newline='')
    ad = csv.writer(f)
    ad.writerow([2, '년도', '인구'])
    f.close()

def csv파일읽기():
    f = open('sample.csv', 'r')
    rd = csv.reader(f)
    for row in rd:
        print(row)
    f.close()

csv파일생성()


