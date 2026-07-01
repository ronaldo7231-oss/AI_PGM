# Google Colab & PyTorch

## Google Colab

### Google Colab이란?

Google Colab(Colaboratory)은 Google에서 제공하는 **클라우드 기반의 Python 개발 환경**입니다.

웹 브라우저만 있으면 별도의 설치 없이 Python 코드를 작성하고 실행할 수 있으며, 머신러닝과 딥러닝 학습에 많이 사용됩니다.

### 특징

- 별도의 Python 설치가 필요 없음
- Jupyter Notebook 환경 제공
- Google Drive와 연동 가능
- GPU, TPU 무료 사용 가능(사용량 제한)
- 코드와 실행 결과를 함께 저장 가능
- 협업 기능 지원

### 장점

- 언제 어디서나 사용 가능
- AI 및 데이터 분석 학습에 적합
- 환경 설정이 필요 없어 초보자도 쉽게 사용 가능

---

# PyTorch

## PyTorch란?

PyTorch는 Meta(Facebook)에서 개발한 **오픈소스 딥러닝 프레임워크**입니다.

Python을 기반으로 하며, 인공지능(AI), 머신러닝(ML), 딥러닝(DL) 모델을 개발하고 학습시키는 데 사용됩니다.

### 특징

- Python 친화적인 문법
- 동적 계산 그래프(Dynamic Computation Graph)
- GPU 연산 지원
- 다양한 딥러닝 라이브러리 제공
- 활발한 커뮤니티와 풍부한 문서

### 주요 활용 분야

- 이미지 분류
- 객체 탐지(Object Detection)
- 자연어 처리(NLP)
- 음성 인식
- 생성형 AI
- 강화학습

---

# 객체지향언어(Object-Oriented Programming, OOP)

## 객체지향언어란?

객체(Object)를 중심으로 프로그램을 설계하는 프로그래밍 패러다임입니다.

현실 세계의 사물을 객체로 표현하여 프로그램을 구성하기 때문에 유지보수와 재사용성이 뛰어납니다.

예를 들어 자동차를 프로그램으로 표현하면,

- 자동차 = 객체(Object)
- 색상 = 속성(Attribute)
- 주행하기 = 메서드(Method)

처럼 표현할 수 있습니다.

---

## 객체(Object)

객체는 **속성(Attribute)** 과 **행동(Method)** 을 함께 가지고 있는 데이터입니다.

```python
car = Car()

car.color
car.drive()
```

---

## 클래스(Class)

클래스는 객체를 생성하기 위한 **설계도(Template)** 입니다.

```python
class Car:
    pass
```

클래스를 이용하여 여러 개의 객체를 생성할 수 있습니다.

```python
car1 = Car()
car2 = Car()
```

---

## 객체지향의 4대 특징

### 1. 캡슐화 (Encapsulation)

데이터와 기능을 하나의 객체로 묶어 외부에서 직접 접근하지 못하도록 보호하는 기능입니다.

장점

- 데이터 보호
- 코드 안정성 향상

---

### 2. 상속 (Inheritance)

기존 클래스의 기능을 물려받아 새로운 클래스를 만드는 기능입니다.

```python
class Animal:
    pass

class Dog(Animal):
    pass
```

장점

- 코드 재사용
- 유지보수 용이

---

### 3. 다형성 (Polymorphism)

같은 메서드라도 객체에 따라 다르게 동작하는 특성입니다.

```python
animal.sound()

Dog → 멍멍
Cat → 야옹
```

장점

- 코드의 유연성 증가

---

### 4. 추상화 (Abstraction)

필요한 기능만 제공하고 내부 구현은 숨기는 개념입니다.

예를 들어 자동차를 운전할 때

- 핸들
- 브레이크
- 엑셀

만 사용하면 되며, 엔진의 내부 동작은 몰라도 운전할 수 있습니다.

---

# 객체지향의 장점

- 코드 재사용성이 높다.
- 유지보수가 쉽다.
- 프로그램 확장이 용이하다.
- 현실 세계를 모델링하기 쉽다.
- 협업에 유리하다.

---

# 객체지향의 단점

- 처음 설계가 어렵다.
- 작은 프로그램에서는 오히려 복잡할 수 있다.
- 절차지향보다 메모리를 더 사용할 수 있다.

---

# 핵심 정리

| 개념 | 설명 |
|------|------|
| Class | 객체를 만들기 위한 설계도 |
| Object | 클래스로부터 생성된 실제 데이터 |
| Attribute | 객체가 가지고 있는 속성 |
| Method | 객체가 수행하는 기능 |
| Encapsulation | 캡슐화 |
| Inheritance | 상속 |
| Polymorphism | 다형성 |
| Abstraction | 추상화 |

---

> 객체지향 프로그래밍(OOP)은 객체를 중심으로 프로그램을 설계하는 방식이며, 코드의 재사용성과 유지보수성을 높이는 현대 프로그래밍의 핵심 개념이다.
