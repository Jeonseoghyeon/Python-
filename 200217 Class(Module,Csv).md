docs.python.org <- 파이썬 문서 모음 Website

RANDOM.ORG <- 진짜 랜덤한 수를 뽑아내는 Website

> Y2K

밀레니엄 버그. 컴퓨터가 2000년 이후의 연도를 제대로 인식하지 못하는 결함. 컴퓨터가 현재 인식하고 있는 연도 표기는 두 자리로 2000년을 00년으로 인식하게 되면 컴퓨터를 사용하는 모든 일이 마비될 수 있어 커다란 재난으로 이어지게 된다. 18세기에 태어난 사람이 다시 살아난 것으로 컴퓨터가 인식할 수도 있고 은행 등 금융권의 이자 계산부터 모든 연산 결과가 왜곡될 수 있다. 또 세금 계산, 계약 만기일 등 날짜와 관련된 일 등 모든 일상 업무에 일대 혼란을 일으키게 된다. 밀레니엄 버그를 Y2k 문제라고도 하는데, Y는 연도(Year)의 첫글자를 딴 것이고 k는 1000(kilo)에서 온 것으로 2000년을 가리킨다.



# 모듈

모듈은 파이썬 정의와 문장들을 담고 있는 파일입니다. 파일의 이름은 모듈 이름에 확장자 `.py`를 붙입니다.

|                        |                                                              |
| ---------------------: | -----------------------------------------------------------: |
|                   모듈 |                       특정 기능을 .py 파일 단위로 작성한 것. |
|                 패키지 | 특정 기능과 관련된 여러 모듈들의 집합. 패키지 안에는 또다른 서브 패키지를 포함 할수도 있음. 보통 인터넷에 있는 패키지를 설치해서 사용 |
| 파이썬 표준 라이브러리 | 파이썬에 기본적으로 설치된 모듈과 내장 함수를 묶어서 파이썬 표준 라이브러리 (Python Standard Library, PSL) 라 함 |
|    pip (패키지 관리자) |           `PyPI` 에 저장된 외부 패키지들을 설치하도록 도와줌 |



### 패키지

- jupyter notebook 파일트리화면에서 New > Folder
- 다음과 같은 폴더구조 생성

```python
myPackage/
    __init__.py
    math/
        __init__.py
        formula.py
    web/
        __init__.py
        url.py
```

> 패키지는 '점으로 구분된 모듈 이름' 을 써서 파이썬의 모듈 이름 공간을 구조화하는 방법입니다. 예를 들어, 모듈 이름 `myPackage.math`는 `myPackage`라는 이름의 패키지에 있는 `math`라는 이름의 서브 모듈을 가리킵니다.

> 단, 파이썬이 디렉터리를 패키지로 취급하게 만들기 위해서 `__init__.py` 파일이 필요합니다. 이렇게 하는 이유는 string 처럼 흔히 쓰는 이름의 디렉터리가, 의도하지 않게 모듈 검색 경로의 뒤에 등장하는 올바른 모듈들을 가리는 일을 방지하기 위함입니다.



### 파이썬 기본 모듈

python에는 기본적으로 제공되는 모듈들이 있습니다.

[표준 라이브러리](https://docs.python.org/ko/3/library/index.html)에서 제공되는 모듈을 확인해보세요!

여기 있는 모든 내용을 외울 필요도 없고, 이런 것이 있다만 확인해보세요 :)

#### 수학 관련 함수(math)

숫자 관련 함수로는 이외에도 분수(frctions), 십진(decimal), 통계(statistics)등이 있습니다.

#### 연산 관련 함수

|                함수 |                            비고 |
| ------------------: | ------------------------------: |
|        math.ceil(x) |                     소수점 올림 |
|       math.floor(x) |                     소수점 내림 |
|       math.trunc(x) |                     소수점 버림 |
| math.copysign(x, y) |        y의 부호를 x에 적용한 값 |
|        math.fabs(x) | float 절대값 - 복소수 오류 발생 |
|   math.factorial(x) |                팩토리얼 계산 값 |
|     math.fmod(x, y) |               float 나머지 계산 |
| math.fsum(iterable) |                        float 합 |
|        math.modf(x) |              소수부 정수부 분리 |



### 난수 발생관련 함수(random)

우리가 사용했던 `random` 역시도 표준라이브러리에서 제공되고 있는 모듈이며, 난수를 발생시키는 모듈입니다.

#### seed

- 경우에 따라서(보통 디버깅 등을 위해 ) 동일한 순서로 난수를 발생시켜야 할 경우가 있다.
- 난수 발생을 위해서는 적절한 시드(seed)를 난수발생기에 주어야 한다.
- 만약 시드가 같다면 동일한 난수를 발생시키게 된다.
- 시드 설정을 하지 않으면 현재 시간을 기반으로 만든다.



### 날짜 관련 모듈(datetime)

### datetime

날짜와 시간의 조합에 관련된 모듈입니다.

(1970년 1월 1일부터 1초씩 증가한다.)

- 어트리뷰트: year, month, day, hour, minute, second, microsecond 및 tzinfo.





# CSV (Comma separated value)

lunch.csv 파일 저장 -> Market place 검색 -> Rainbow or Excel CSV 다운



![image-20200217104718647](200217 Class(Module,OOP).assets/image-20200217104718647.png)



```python
csvfile = open('lunch.csv','w', encoding='utf-8', newline = '')

 # 없으면 자동으로 생성해줌 / 'w' : 쓰기모드 / encoding='utf-8' : 한국어로 할 수 있도록 / newline : 엔터 쳐져서 출력되는 것 수정
csv_writer = csv.writer(csvfile)

#데이터 입력
csv_writer.writerow(['Hello']) # 코드로 파일을 바꾸고 있음
for key,value in lunch.items():
    csv_writer.writerow([key,value])
csvfile.close()
```



```python
with open('lunch.csv','w', encoding='utf-8', newline = '') as csvfile:  # close 따로 안해줘도 된다. 위에 놈과 똑같은 것
    
    csv_writer = csv.writer(csvfile)

    #데이터 입력
    csv_writer.writerow(['Hello']) # 코드로 파일을 바꾸고 있음
    for key,value in lunch.items():
        csv_writer.writerow([key,value])
```



<실습>

```python
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


rank_dict = {}
for idx, rank in enumerate(rankings,1): # idx 값 1부터 시작!!!
    rank_dict[f'{idx}위'] = rank.text

print(rank_dict)

with open('daum.csv','w', encoding = 'utf-8', newline= '') as csvfile: # r, w , a 세가지 옵션이 있다. read, write, append
    csv_writer = csv.writer(csvfile)
    for key,val in rank_dict.items():
        csv_writer.writerow([key,val])
```



빈 list를 만든 뒤 Dict 구조를 이용한 요소들을 추가시킨다.

```python
rank_list = []
for idx,rank in enumerate(rankings,1):
    rank_dict = {
        'rank':f'{idx}위',
        'value': rank.text
    }
    rank_list.append(rank_dict)

print(rank_list)
```





<멜론 Top 100>

![image-20200217140405026](200217 Class(Module,OOP).assets/image-20200217140405026.png)

Network - Headers - User_agent 복사



```python
import requests

url = 'https://www.melon.com/chart/index.htm'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

headers = {
    'User-agent':user_agent
}
res = requests.get(url,headers=headers)
print(res)
```

이렇게 해야 <Response [406]>이 아닌 <Response [200]>이 뜬다.

```python
import requests
import csv
from bs4 import BeautifulSoup
url = 'https://www.melon.com/chart/index.htm'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
headers = {
    'User-Agent' : user_agent,
}
res = requests.get(url, headers = headers).text
rank_list = []
rank_dict = []
html = BeautifulSoup(res,'html.parser')
rankings = html.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
singers = html.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > span')
for idx in range(len(rankings)):
    rank_dict = {
        'rank' : f'{idx+1}위',
        'value' : rankings[idx].text,
        'singer' : singers[idx].text
    }
    rank_list.append(rank_dict)
    print(rank_dict)
with open('melonrank.csv','w', encoding='utf-8',newline='') as csvfile:
    fieldnames = ['rank', 'value', 'singer']
    csv_writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    csv_writer.writeheader()
    for rank1 in rank_list:
        csv_writer.writerow(rank1)
```



# Errors and Expectations

### 문법 에러 (Syntax Error) : 예외처리 불가

가장 많이 만날 수 있는 에러로 발생한 `파일 이름`과 `줄번호`, `^` 문자 을 통해 파이썬이 읽어 들일 때(parser)의 문제 발생 위치를 표현합니다.

`parser` 는 문제가 되는 줄을 다시 보여주고 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 작은 '화살표(`^`)'를 표시합니다.



### 예외 (Exceptions)

- 문법이나 표현식이 바르게 되어있지만, 실행시 발생하는 에러다.
- 아래 제시된 모든 에러는 Exception을 상속받아 이뤄진다.
- 

## 예외 처리

#### 기본 - `try` `except`

`try` 구문을 이용하여 예외 처리를 할 수 있습니다.

**활용법**

```python
try:
    codeblock1
except 예외:
    codeblock2
```

- `try`절이 실행된다.
- 예외가 발생되지 않으면, `except`없이 실행이 종료 된다.
- 예외가 중간에 발생하면, **남은 부분을 수행하지 않고**, `except`가 실행된다.

