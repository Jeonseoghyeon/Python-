# startcamp day2

### API

> 요청과 응답을 통해서 다른 기능을 끌어올 때 사용



### 주소의 구성

> 주소 `?` Key=Value &`%`~~ query=삼성 

```python
url = 'https://search.naver.com/search.naver?query='
key_words = ['아이유','박신혜','위너','ITZY','BTS']

for key_word in key_words:
    print(key_word)

for key_word in key_words:
    webbrowser.open(url + key_word)
    
```

- webbrowser.open()

- webbrowser.open_new()
- webbrowser.open_new_tab()



### 웹에서 끌어오기

- 우클릭 - 검사

```python
import requests
from bs4 import BeautifulSoup

sise_url = 'https://finance.naver.com/sise'

res = requests.get(sise_url).text
soup = BeautifulSoup(res,'html.parser')


kospi = soup.select_one('#KOSPI_now') # //'#'은 ID
print(kospi.text)

```

<img src="C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200116110641044.png" alt="image-20200116110641044" style="zoom: 33%;" />



```python
#Dollar 끌어오기(내가 한 실습)

import requests
from bs4 import BeautifulSoup

dollar_url = 'https://finance.naver.com/marketindex/'

res = requests.get(dollar_url).text

soup = BeautifulSoup(res,'html.parser')

#exchangeList > li.on > a.head.usd > div > span.value

dollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value') 

print(dollar.text)

```



- BeautifulSoup

  .select(selector) : 여러개

  .select(selector_one) : 첫 하나만





### HTML

- 머리와 몸으로 나누어져 있음(Head, Body)
  - Head : 타이틀/정보 등
    - Title : 탭의 제목
- Body : 실제로 보여지는 부분
- 웹에서 F12 -> 개발자 환경 -> 조작 -> F5 : 복귀

```HTML
# HTML : HyperText Markup Language

<!DOCTYPE html>
<html>
    <head>
        <title>여기는 html실습을 위한 페이지입니다.</title>

    </head>
    <body>
        <h1>HTML!!!</h1>
        <h2>작은 글씨입니다.</h2>
        <h3>후헤헤헤</h3>
        <h4>하하호호히히</h4>
        <h5>꺄르르르르</h5>
        <h6>우앙이제끝</h6>

        <ul>
            <li>안녕하세용</li>
            <li>반갑습니당</li>

        </ul>
        
        <ol>
            <li>첫번째</li>
            <li>두번째</li>
        </ol>

        <a href="http://www.naver.com">네이버</a>
    </body>
</html>
```

- ul : unordered list / ol : ordered list / li : list

- h1~6 : heading 1~6

  - ​	a : anchor / href(hyperlist reference)
- 주석 : <!-- -->



### 기타

- ctrl + ` => 터미널 창 열기

- 회색 => 저장이 안됐어요!

- <img src="C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200116102816909.png" alt="image-20200116102816909" style="zoom: 25%;" />

  왼쪽 : 윈도우 탐색기 / 중간 : 코딩하는 공간 
  
  ls => 폴더 내 파일 보여줌
  
  cd 폴더명 => Change direction(폴더 이동) / cd.. => 이전으로
  
  ctrl + c = 벗어나기

- Debug mode : 개발자 모드
  
  - On이 됐을 때는 계속 벗어나고 들어오지 않아도 Real-time으로 반영 됨.



# 코드들

``` 
import requests
from bs4 import BeautifulSoup

sise_url = 'https://finance.naver.com/sise'

res = requests.get(sise_url).text
soup = BeautifulSoup(res,'html.parser')


kospi = soup.select_one('#KOSPI_now')
print(kospi.text)


```



```
import requests
from bs4 import BeautifulSoup

dollar_url = 'https://finance.naver.com/marketindex/'

res = requests.get(dollar_url).text

soup = BeautifulSoup(res,'html.parser')

#exchangeList > li.on > a.head.usd > div > span.value

dollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value') 

print(dollar.text)

```

```
from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return '반갑습니다'

@app.route('/') 
def hello():
    name = request.args.get("name", "World")
    return f'안녕하세요, {escape(name)}!'


@app.route('/html_tag')
def html_tag():
    return """
    <h1>헤딩 1번입니다.</h1>
    <ul>
        <li>안녕하세요</li>
        <li>반갑습니다</li>
    </ul>
"""

@app.route('/first')
def first():
    return render_template('hello.html')

@app.route('/movies')
def movies():
    movies = ['해치지않아','닥터 두리틀', '나쁜녀석']
    return render_template('movies.html', movies = movies)

@app.route('/company')
def com():    
    return render_template('com.html')

    return render_template('ping.html')

    
@app.route('/recom_com')
def recom_com():
    location = request.args.get("location")
    companies = ['삼성전자','SK하이닉스','현대자동차','LG전자']
    Random_company = random.choice(companies)
    Random_company_dict ={
        '삼성전자': 'https://post-phinf.pstatic.net/MjAxOTExMTRfOTUg/MDAxNTczNjg5NzM0NDE0.4N9ipkkZvZQc-g-vJOdWJRj95acANd_lwBbwpXHUqhYg.LKxB0eW8W0wKR6qhPFmGL5RYZbb0jWxJ12K89QwrRsAg.JPEG/48571_42978_4724.jpg?type=w1200',
        'SK하이닉스': 'https://post-phinf.pstatic.net/MjAxOTExMTRfMjU5/MDAxNTczNjg5NzM2OTQz.QE-KatlNOtSpBvoaU85TiKzny63DmHWUGmAKmnoGD6Mg.p9N5qg6TxPeiakklxxsvk7t0OQ_A29a7-rJeMH7iQDAg.PNG/48288_42688_1641.png?type=w1200',
        '현대자동차': 'http://cafefiles.naver.net/20140911_203/sdfh2000_1410441635132LXcqH_PNG/%C7%F6%B4%EB%C0%DA%B5%BF%C2%F7_%C3%A4%BF%EB_%B8%B6%B0%A8_%B7%CE%B0%ED.PNG',
        'LG전자': 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=LG%EC%A0%84%EC%9E%90&oquery=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&tqi=UAsOksprvTossCdC0D4ssssssRR-245435#'
    }
    Rcd = Random_company_dict[Random_company]
    return render_template('recom_com.html',Random_company = Random_company, location = location, Rcd = Rcd)
    


@app.route('/pong')
def pong():
    location = request.args.get("location")
    return render_template('pong.html',location=location)

@app.route('/name/<string:name>')
def name(name):
    return render_template('name.html',html_name = name)

@app.route('/lunch')
def lunch():
    menu = ['소고기','돼지고기','닭고기','말고기','양고기']
    menu_dict = {
        '소고기': 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%86%8C#',
        '돼지고기': 'https://search.naver.com/search.naver?where=image&query=%EB%8F%BC%EC%A7%80&ie=utf8&sm=tab_she&qdt=0#',
        '닭고기': 'https://search.naver.com/search.naver?where=image&query=%EB%8B%AD&ie=utf8&sm=tab_she&qdt=0#',
        '말고기': 'https://search.naver.com/search.naver?where=image&query=%EB%A7%90&ie=utf8&sm=tab_she&qdt=0#',
        '양고기': 'https://search.naver.com/search.naver?where=image&query=%EC%96%91&ie=utf8&sm=tab_she&qdt=0#'
        }
    Random_menu = random.choice(menu)
    Random_menu_image = menu_dict[Random_menu]

return render_template('lunch.html',RM = Random_menu, RM_I = Random_menu_image)







@app.route('/cube/<int:num>')
def cube(num):
    cube_num = num * num * num
    return render_template('cube.html',html_num = num, html_cube_num = cube_num)


if __name__ == '__main__':
    app.run(debug=True)


FLASK_APP=hello.py flask run
 * Serving Flask app "hello"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>나와 어울리는 회사는?</title>
</head>
<body>
    <h1>나와 어울리는 회사는?</h1>
    <form action = "/recom_com"> 
        이름 <input name = "location"> <input type = "submit">
    </form>

</body>
</html>
```

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>축하합니다!!</title>
</head>
<body>
    <h1>{{location}}님 상반기 가즈아~!~!</h1>
    {{Random_company}}<br>

    <img src={{Rcd}} alt="My Image">
</body>
</html>
```

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>나와 어울리는 회사는?</title>
</head>
<body>
    <h1>나와 어울리는 회사는?</h1>
    <form action = "/com"> 
        이름 <input name = "location"> <input type = "submit">
    </form>

</body>
</html>
```

```
<!DOCTYPE html>
<html>
<head>

</head>
<body>
    <h1>오늘의 추천 메뉴 : {{RM}}</h1>
    <h1><img src="RM_I" alt="My Image"></h1>
</body>
</html>
```

