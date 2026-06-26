# 🐍 Python List(리스트)

> Python의 리스트(List)에 대해 정리한 학습 노트입니다.

---

# 📚 목차

* 리스트(List)란?
* 리스트 생성하기
* 인덱스(Index)
* 슬라이싱(Slicing)
* 리스트 수정
* 리스트 추가
* 리스트 삭제
* 리스트 주요 함수
* 반복문과 리스트
* 리스트 컴프리헨션(List Comprehension)
* 2차원 리스트
* 리스트 복사
* 자주 발생하는 오류
* 정리

---

# 1. 리스트(List)란?

리스트(List)는 여러 개의 데이터를 하나의 변수에 저장할 수 있는 **순서가 있는(Mutable)** 자료형입니다.

## 특징

* 순서(Index)가 존재한다.
* 중복된 값을 저장할 수 있다.
* 서로 다른 자료형을 함께 저장할 수 있다.
* 값을 수정할 수 있다(Mutable).

```python
numbers = [1, 2, 3, 4, 5]

fruits = ["apple", "banana", "orange"]

mixed = [1, "Python", True, 3.14]
```

---

# 2. 리스트 생성하기

## 빈 리스트

```python
empty = []
```

또는

```python
empty = list()
```

## 값이 있는 리스트

```python
numbers = [10, 20, 30]

names = ["Tom", "Jane", "Mike"]
```

---

# 3. 인덱스(Index)

리스트는 **0부터 시작하는 인덱스**를 사용합니다.

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

출력

```
apple
banana
orange
```

### 음수 인덱스

```python
print(fruits[-1])
```

출력

```
orange
```

---

# 4. 슬라이싱(Slicing)

형식

```python
리스트[start:end]
```

예제

```python
numbers = [10,20,30,40,50]

print(numbers[1:4])
```

출력

```
[20, 30, 40]
```

다양한 슬라이싱

```python
numbers[:3]

numbers[2:]

numbers[::2]

numbers[::-1]
```

결과

```
[10,20,30]

[30,40,50]

[10,30,50]

[50,40,30,20,10]
```

---

# 5. 리스트 수정

리스트는 값을 변경할 수 있습니다.

```python
fruits = ["apple","banana","orange"]

fruits[1] = "melon"

print(fruits)
```

출력

```
['apple', 'melon', 'orange']
```

---

# 6. 리스트 추가

## append()

맨 뒤에 추가

```python
fruits.append("kiwi")
```

---

## insert()

원하는 위치에 추가

```python
fruits.insert(1, "grape")
```

---

## extend()

여러 개 추가

```python
fruits.extend(["pear", "peach"])
```

---

# 7. 리스트 삭제

## remove()

값으로 삭제

```python
fruits.remove("banana")
```

---

## pop()

마지막 요소 삭제

```python
fruits.pop()
```

인덱스를 지정할 수도 있습니다.

```python
fruits.pop(1)
```

---

## del

```python
del fruits[0]
```

---

## clear()

전체 삭제

```python
fruits.clear()
```

---

# 8. 리스트 주요 함수

| 함수             | 설명         |
| -------------- | ---------- |
| len()          | 길이         |
| max()          | 최대값        |
| min()          | 최소값        |
| sum()          | 합계         |
| sorted()       | 정렬된 리스트 반환 |
| list.sort()    | 원본 리스트 정렬  |
| list.reverse() | 리스트 뒤집기    |
| count()        | 개수         |
| index()        | 위치 찾기      |

예제

```python
numbers = [3,1,5,2,4]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
```

---

# 9. 반복문과 리스트

```python
fruits = ["apple","banana","orange"]

for fruit in fruits:
    print(fruit)
```

또는

```python
for i in range(len(fruits)):
    print(i, fruits[i])
```

---

# 10. 리스트 컴프리헨션(List Comprehension)

기존 방식

```python
result = []

for i in range(5):
    result.append(i)
```

리스트 컴프리헨션

```python
result = [i for i in range(5)]
```

조건도 사용할 수 있습니다.

```python
even = [x for x in range(10) if x % 2 == 0]
```

결과

```
[0,2,4,6,8]
```

---

# 11. 2차원 리스트

```python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
```

접근

```python
print(matrix[1][2])
```

출력

```
6
```

---

# 12. 리스트 복사

잘못된 방법

```python
a = [1,2,3]

b = a
```

`b`를 수정하면 `a`도 함께 변경됩니다.

올바른 방법

```python
b = a.copy()
```

또는

```python
b = a[:]
```

---

# 13. 자주 발생하는 오류

## IndexError

```python
numbers = [1,2,3]

print(numbers[5])
```

오류

```
IndexError: list index out of range
```

---

## ValueError

```python
numbers.remove(100)
```

오류

```
ValueError
```

---

# 14. 리스트와 튜플의 차이

| 리스트         | 튜플           |
| ----------- | ------------ |
| []          | ()           |
| 수정 가능       | 수정 불가능       |
| append() 가능 | append() 불가능 |
| Mutable     | Immutable    |

---

# 15. 정리

✔ 리스트는 가장 많이 사용하는 자료형이다.

✔ 순서(Index)가 존재한다.

✔ 값을 수정할 수 있다.

✔ append(), insert(), remove(), pop()은 반드시 익혀두자.

✔ 반복문과 함께 사용하면 매우 강력하다.

✔ 리스트 컴프리헨션은 Python다운 코드를 작성하는 핵심 문법이다.



# 🐍 Python Container(컨테이너)

> Python에서 사용하는 대표적인 컨테이너(Container) 자료형을 정리한 학습 노트입니다.

---

# 📚 목차

* 컨테이너(Container)란?
* 컨테이너의 특징
* 컨테이너의 종류
* List
* Tuple
* Dictionary
* Set
* 컨테이너 비교
* 반복문과 컨테이너
* 중첩 컨테이너
* 어떤 컨테이너를 사용해야 할까?
* 정리

---

# 1. 컨테이너(Container)란?

컨테이너(Container)는 **여러 개의 데이터를 하나의 객체에 저장하고 관리하는 자료형**입니다.

쉽게 말하면,

> **"여러 개의 데이터를 담을 수 있는 그릇"**

이라고 생각하면 됩니다.

예를 들어 학생 5명의 점수를 저장한다고 하면,

## 일반 변수

```python
score1 = 90
score2 = 85
score3 = 100
score4 = 95
score5 = 88
```

## 컨테이너 사용

```python
scores = [90, 85, 100, 95, 88]
```

컨테이너를 사용하면 데이터를 훨씬 효율적으로 관리할 수 있습니다.

---

# 2. 컨테이너의 특징

* 여러 개의 데이터를 하나의 변수에 저장할 수 있다.
* 반복문과 함께 사용하기 편리하다.
* 데이터 검색이 쉽다.
* 데이터를 추가하거나 삭제할 수 있다.
* 다양한 자료형을 함께 저장할 수 있다.

예제

```python
data = [100, "Python", True, 3.14]
```

---

# 3. Python의 대표적인 컨테이너

Python에서 가장 많이 사용하는 컨테이너는 다음 네 가지입니다.

| 컨테이너       | 문법             |      순서      |   중복  | 수정 가능 |
| ---------- | -------------- | :----------: | :---: | :---: |
| List       | `[]`           |       O      |   O   |   O   |
| Tuple      | `()`           |       O      |   O   |   X   |
| Dictionary | `{key: value}` | O (삽입 순서 유지) | Key X |   O   |
| Set        | `{}`           |       X      |   X   |   O   |

---

# 4. List (리스트)

가장 많이 사용하는 컨테이너입니다.

```python
fruits = ["apple", "banana", "orange"]
```

## 특징

* 순서(Index)가 존재한다.
* 수정 가능(Mutable)
* 중복 저장 가능
* 다양한 자료형 저장 가능

```python
fruits.append("kiwi")

print(fruits)
```

출력

```text
['apple', 'banana', 'orange', 'kiwi']
```

사용 예

* 학생 성적
* 쇼핑 목록
* 게임 아이템
* 센서 데이터

---

# 5. Tuple (튜플)

튜플은 리스트와 거의 같지만 **수정할 수 없는(Immutable)** 자료형입니다.

```python
point = (10, 20)
```

값은 읽을 수 있지만 수정은 불가능합니다.

```python
print(point[0])
```

```python
point[0] = 100
```

출력

```text
TypeError
```

사용 예

* 좌표
* RGB 색상
* 날짜
* 변경되면 안 되는 데이터

---

# 6. Dictionary (딕셔너리)

Dictionary는 **Key와 Value**를 함께 저장하는 자료형입니다.

```python
student = {
    "name": "Tom",
    "age": 20,
    "major": "Computer"
}
```

데이터 접근

```python
print(student["name"])
```

출력

```text
Tom
```

데이터 추가

```python
student["grade"] = 4
```

사용 예

* 회원 정보
* JSON 데이터
* 설정(Config)
* API 응답 데이터

---

# 7. Set (집합)

Set은 **중복을 허용하지 않는 컨테이너**입니다.

```python
numbers = {1, 2, 3, 2, 1}
```

출력

```text
{1, 2, 3}
```

## 특징

* 순서가 없다.
* 중복을 허용하지 않는다.
* 집합 연산이 가능하다.

예제

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A & B)   # 교집합
print(A | B)   # 합집합
print(A - B)   # 차집합
```

출력

```text
{3}
{1, 2, 3, 4, 5}
{1, 2}
```

사용 예

* 중복 제거
* 태그 관리
* 회원 ID 중복 확인

---

# 8. 컨테이너 비교

| 특징     | List  | Tuple | Dictionary | Set   |
| ------ | ----- | ----- | ---------- | ----- |
| 순서 존재  | O     | O     | O          | X     |
| 인덱스 사용 | O     | O     | X          | X     |
| 수정 가능  | O     | X     | O          | O     |
| 중복 허용  | O     | O     | Key X      | X     |
| 검색 방식  | Index | Index | Key        | Value |

---

# 9. 반복문과 컨테이너

## List

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

---

## Dictionary

```python
student = {
    "name": "Tom",
    "age": 20
}

for key, value in student.items():
    print(key, value)
```

---

## Set

```python
numbers = {1, 2, 3}

for num in numbers:
    print(num)
```

---

# 10. 중첩 컨테이너

컨테이너 안에는 또 다른 컨테이너를 저장할 수 있습니다.

## 리스트 안에 리스트

```python
students = [
    ["Tom", 90],
    ["Jane", 95],
    ["Mike", 88]
]
```

## 딕셔너리 안에 리스트

```python
student = {
    "name": "Tom",
    "scores": [90, 80, 100]
}
```

## 리스트 안에 딕셔너리

```python
students = [
    {"name": "Tom", "score": 90},
    {"name": "Jane", "score": 95}
]
```

중첩 컨테이너는 실제 프로젝트에서 매우 자주 사용됩니다.

---

# 11. 어떤 컨테이너를 사용해야 할까?

| 상황           | 추천 컨테이너    |
| ------------ | ---------- |
| 순서대로 데이터를 저장 | List       |
| 변경되지 않는 데이터  | Tuple      |
| 이름과 값을 함께 저장 | Dictionary |
| 중복 제거        | Set        |

예를 들어 학생 정보를 저장한다면,

```python
student = {
    "name": "Kim",
    "age": 25,
    "scores": [90, 85, 100],
    "subjects": {"Python", "Java"}
}
```

처럼 여러 컨테이너를 함께 사용할 수 있습니다.

---

# 12. 핵심 정리

| 컨테이너       | 핵심 특징                      |
| ---------- | -------------------------- |
| List       | 가장 많이 사용하는 자료형, 순서 O, 수정 O |
| Tuple      | 읽기 전용 데이터 저장               |
| Dictionary | Key-Value 형태의 데이터 저장       |
| Set        | 중복 제거 및 집합 연산              |

---

# 🎯 언제 어떤 컨테이너를 사용할까?

* **List** → 순서가 중요하고 데이터를 자주 추가·삭제할 때
* **Tuple** → 변경되지 않는 데이터를 저장할 때
* **Dictionary** → 이름과 값처럼 짝을 이루는 데이터를 저장할 때
* **Set** → 중복을 제거하거나 집합 연산을 수행할 때

---

# 📌 마무리

컨테이너는 Python 프로그래밍의 핵심 자료형입니다.

프로그램을 작성하다 보면 대부분의 데이터는 **List**, **Tuple**, **Dictionary**, **Set** 중 하나로 관리하게 됩니다. 각 컨테이너의 특징을 이해하고 상황에 맞게 선택하면 더 효율적이고 읽기 쉬운 코드를 작성할 수 있습니다.

