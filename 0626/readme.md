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
