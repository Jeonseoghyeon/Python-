import requests
from bs4 import BeautifulSoup
import csv


url = 'https://www.melon.com/chart/index.htm'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

headers = {
    'User-agent':user_agent
}
res = requests.get(url,headers=headers).text
html = BeautifulSoup(res,'html.parser')
titles = html.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
# print(titles)

melon_list = []
for idx, title in enumerate(titles,1):
    sing_dict = {'rank':f'{idx}위','title':title.text,}
    melon_list.append(sing_dict)
    print(sing_dict)


rankings = html.select('#frm > div > table > tbody > tr > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
singers = html.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > span')
# print(singers)


# with open('melon.csv','w',encoding='utf-8',newline='') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     for ind,val in enumerate(rankings,1):
#         csv_writer.writerow([ind,val.text])
#     for index,value in enumerate(singers,1):
#         print(index,value.text,end='')
