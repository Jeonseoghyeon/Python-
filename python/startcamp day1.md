# startcamp day1

### 프로그래밍 3형식

1. 저장

2. 조건

3. 반복

   

##### 저장

> 저장은 박스에 값,문자열 등을 넣어서 보관하는 방식이라고 생각하면 된다.

- 글자, 숫자, True, Flase
- 리스트
- 딕셔너리

##### 조건

> 조건문은 **if**, else, **elif** 로 구성된다.

###  

##### 반복

- `while`문을 이용한 반복문

```python
n = 0
While n<3
    print('출력)
    n = n + 1
```

- `for`문을 이용한 반복문

```python
dust = [10,20,30]
for i in dust:
    print(dust)
```



### 챗봇 만들기

- 미세먼지

```python
import requests
from bs4 import BeautifulSoup


url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'.format(key)


request = requests.get(url).text 
soup = BeautifulSoup(request,'xml')
item = soup('item')[5]
time = item.dataTime.text
dust = int(item.pm10Value.text)

conc = ''

if dust > 150 : 
  conc='매우나쁨'
elif 80 < dust <=150 :
  conc='나쁨'
elif 30 <dust<=80  :
  conc='보통'
else:
  conc='좋음'
  
  
# dust 변수에 들어 있는 내용을 출력해보세요.
print('{} 기준 미세먼지 농도는 {}({})입니다.'.format(time, dust,conc))

# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.
```

- 점심메뉴

> Random 함수 : Choice(한 개 선별), Sample(여러 개 선별) / Import 필요
>
> Dictionary : 견출지 붙인 Box들의 묶음 (Index로 하지 않음.. Key를 입력해야 함.)

```python
# menu 리스트를 만들어주세요.

import random


print("오늘의 추천 메뉴!")

menu_list = ['매운돈가스', '옛날짜장면' ]
menu_dict = {'짜장면':'062-123-1234', '매운돈가스':'062-789-7890' }


a = random.choice(menu_list)
            
if a == '매운돈가스':
    print("{}, {}".format('매운돈가스', menu_dict['매운돈가스']))
else:
    print("{}, {}".format('옛날짜장면', menu_dict['짜장면']))       
```



- 기타

  Python : for i in 리스트~ 에서 i는 리스트를 받았을 때 index로 처리한다.

  Fspring : Python 3.7부터 나온 기능 : Format 함수, %d/%s 등을 대신하는 것

  While보단 For을 많이 쓴다.

  ### `API(???????)`

  프로토콜 : 규약 (Http://~ : 나는 http라는 규약을 통해 통신할거야!)



### Markdown 정리 법

- ctrl + / : 원본 '보기
- ''' + enter => 코드블락
- '>' => 얇게 설명하는 것
- '-' => 검정 동그라미
- '#' 헤딩(갯수 많을수록 크기 작아짐)

- 'Shift + Tab' => 왼쪽으로 쭉 가기



### 기타 참고하면 좋을 것들

- YOLO
- 유포니아
- Teachable machine
- AWS button
- Sentiment Analysis