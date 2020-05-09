# OOP(객체 지향 프로그래밍)

- Attribute : 속성(오창희,광주 등)
- Method : 행위(함수 : 수업하기, 밥먹기 등)

- class : 객체를 의미한다.



dir() 쓰면 해당 객체가 가지고 있는 Methods를 볼 수 있다.



### 클래스 및 인스턴스

Class 정의할 때 PASCAL_CASE를 적용할 것이다. (대문자)

#### 클래스 정의하기 (클래스 객체 생성하기)

- 선언과 동시에 클래스 객체가 생성된다.
- 또한, 선언된 공간은 지역 스코프(local scope)로 사용된다.
- 정의된 어트리뷰트 중 변수는 멤버 변수로 불린다.
- 정의된 함수(`def`)는 메서드로 불린다.

------

**활용법**

```python
class ClassName:
    attributes
    methods
```



#### 인스턴스 생성하기

인스턴스가 생성되었을 때는 아무런 Data도 없는 상태이다.

- 인스턴스 객체는 `ClassName()`을 호출함으로써 생성된다.
- 인스턴스 객체와 클래스 객체는 서로 다른 이름 공간을 가지고 있다.
- **인스턴스(instance) => 클래스(class) => 전역(global) 순으로 탐색을 한다.**

```python
# 인스턴스 = 클래스()
puppy = Dog()
```

- 클래스는 특정 개념을 표현하는 껍데기고 실제 사용하려면 인스턴스를 생성해야 한다.



```python
    def change_password(self, old, new): # Self는 알아서 들어가는 것.
        if old == self.password:
            self.password = new
            print('변경 완료')
        else:
            print('비밀번호가 다릅니다.')
```

```python
Jeon.change_password('gkdld','asdf') # Self에 해당하는 Parameter 넣어주지 안아도 됨.
print(Jeon.password)
```



정보를 자기 자신한테서 먼저 찾아보고 없으면 원본 데이터에서 찾는다.



# OOP advanced

데코레이터는 함수랑 떨어져 있으면 안된다.