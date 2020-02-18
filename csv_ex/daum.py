import requests # Requests 모듈 임포트
from bs4 import BeautifulSoup # 깔끔하게 변환해주는 놈
import csv

url = 'https://www.daum.net'

res = requests.get(url).text  #res = response , [200] ==> .text 추가해주면 txt 내용

html = BeautifulSoup(res,'html.parser') #예쁘게 바꿔줭
# print(html)
rankings = html.select('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini.hide > div.hotissue_layer > ol > li > div > div:nth-child(1) > span.txt_issue > a')

# with open('daum.csv','w', encoding='utf-8', newline = '') as csvfile:
#     csv_writer = csv.writer(csvfile)
    # for ind,val in enumerate(rankings,1):
    #     rank = str(ind) + '위'
    #     csv_writer.writerow([rank,val.text])
    #     print(val)

''' dict 이용 
# rank_dict = {}
# for idx, rank in enumerate(rankings,1): # idx 값 1부터 시작!!!
#     rank_dict[f'{idx}위'] = rank.text

# with open('daum.csv','w', encoding = 'utf-8', newline= '') as csvfile: # r, w , a 세가지 옵션이 있다. read, write, append
#     csv_writer = csv.writer(csvfile)
#     for key,val in rank_dict.items():
#         csv_writer.writerow([key,val])
'''


rank_list = []
for idx,rank in enumerate(rankings,1):
    rank_dict = {
        'rank':f'{idx}위',
        'value': rank.text
    }
    rank_list.append(rank_dict)

with open('daum.csv','w',encoding='utf-8',newline='') as csvfile:
    # csv_writer = csv.writer(csvfile)
    fieldnames = ['rank','value'] #key값 순서대로 적은 것
    csv_writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    csv_writer.writeheader()
    for rank in rank_list:
        csv_writer.writerow(rank)
        

# {
#     '8위':'제주공항',
#     '10위':'손예진'
# }
# [
#     {
#         'rank':'1위',
#         'value':'제주공항'
#     },
#     {
#         'rank':'2위',
#         'value':'손예진',
#         '연관검색어':'현빈'
#     }
# ]