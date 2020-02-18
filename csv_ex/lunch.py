import csv

lunch = {
    '그릴스' : '매운돈까스',
    '소반' : '낙곱새',
    }

'''
csvfile = open('lunch.csv','w', encoding='utf-8', newline = '')

 # 없으면 자동으로 생성해줌 / 'w' : 쓰기모드 / encoding='utf-8' : 한국어로 할 수 있도록 / newline : 엔터 쳐져서 출력되는 것 수정
csv_writer = csv.writer(csvfile)

#데이터 입력
csv_writer.writerow(['Hello']) # 코드로 파일을 바꾸고 있음
for key,value in lunch.items():
    csv_writer.writerow([key,value])
csvfile.close()
'''

with open('lunch.csv','w', encoding='utf-8', newline = '') as csvfile:  # close 따로 안해줘도 된다. 위에 놈과 똑같은 것
    
    csv_writer = csv.writer(csvfile)

    #데이터 입력
    csv_writer.writerow(['Hello']) # 코드로 파일을 바꾸고 있음
    for key,value in lunch.items():
        csv_writer.writerow([key,value])