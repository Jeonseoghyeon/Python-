### 1번 : Python intro

-내장함수 docstring 확인 코드

```python
(method_name).__doc__
```

-n진수 10진수로 출력하는 코드

```python
binary_number = 0b10
octal_number = 0o10
decimal_number = 10
hex_number = 0xF

print(binary_number, octal_number, decimal_number, hex_number)
```

-isclose 확인 코드

```python
import math # math module import
math.isclose(a,b)
```

-튜플, 리스트 등은 +로 합칠 수 있다.

-List slicing

```python
a = [1,2,3,4,5]
a_list[::-1] #Output : [5,4,3,2,1]
a_list[::2] #Output : [1,3,5]
a_list[:-1] #Output : [1,2,3,4]
```

-Set

세트는 중괄호로 처리 {}

순서가 없고 중복된 값이 없다. (중복값 제거할 때 사용)

빈 집합을 만드려면 `set()`를 사용해야 한다!!!



### 2번 : Control_of_flow

-조건 표현식

```python
#true_value if <조건식> else false_value
#예시
num = int(input('숫자를 입력하세요 : '))

print('0 보다 큼') if num > 0 else print('0 보다 크지않음')

```

