# len함수 및 문자열의 칸
#a = "Life is too short, You need Python"
#print(len(a))
#print(a[3])
#print(a[0:4])
#print(a[0])


# 숫자, 문자열 포매팅          "%d" %(,)
#b=3
#c=5
#print("I eat %d apples and %d oranges."%(b,c))
#print("I eat %d apples and %f oranges."%(b,3.141592))
#print("I eat %d apples and %.2f oranges."%(b,3.141592))
#print("I eat %s apples." % "five")

#str1=" Sample python string"
#print(str1)
#print("example string : %s " %str1)

# 포맷함수를 이용한 포매팅      "{}".format(,)
#print("I eat {0} apples, {1} oranges and {2} grapes.".format(3,5,5+3))

# print 와 print(f) 차이
#print("I eat 3 apples and 5 oranges.")
#print("I eat {0} apples and {1} oranges.".format(3,5))
#print(f"I eat 3 apples and 5 oranges.")
#print(f"I eat {1+2} apples and {2+3} oranges.")

# 키보드로부터 입력 받는 함수 input
#a=int(input("Enter first number: "))
#b=int(input("Enter second number: "))
#print(f"You entered: {a} and {b} ")
#print(f"a+b={(a)+(b)}")
#print(f"a-b={(a)-(b)}")
#print(f"a*b={(a)*(b)}")
#print(f"a/b={(a)/(b)}")


#1. 두개의 정수를 입력받아 사칙연산의 결과를 출력하세요.
#a=int(input("Enter first number: "))
#b=int(input("Enter second number: "))
#print(f"You entered: {a} and {b} ")
#print(f"a+b={(a)+(b)}")
#print(f"a-b={(a)-(b)}")
#print(f"a*b={(a)*(b)}")
#print(f"a/b={(a)/(b)}")

#2. 5개의 정수값을 입력받아 리스트에 저장하고 그 리스트의 합, 평균, 최소값, 최대값을 출력하세요.
#a=int(input("Enter first number: "))
#b=int(input("Enter second number: "))
#c=int(input("Enter third number: "))
#d=int(input("Enter fourth number: "))
#e=int(input("Enter fifth number: "))

#g=[a,b,c,d,e]
#print(f"sum : {sum(g)}")
#print(f"avg : {sum(g)/len(g)}")
#print(f"min : {min(g)}")
#print(f"max : {max(g)}")

#3. 과일명이 있는 리스트를 정의하고, 그 리스트의 첫번째와 마지막 문자열을 출력하세요.

#fruits=[]
#fruit = input("Enter a fruit: ")
#fruits.append(fruit)
#fruit = input("Enter a fruit: ")
#fruits.append(fruit)
#fruit = input("Enter a fruit: ")
#fruits.append(fruit)
#fruit = input("Enter a fruit: ")
#fruits.append(fruit)
#fruit = input("Enter a fruit: ")
#fruits.append(fruit)
#print(fruits)
#print(fruits[0])
#print(fruits[-1])

#dict1={1:"apple","ba":"banana"}
#print(dict1[1])
#print(dict1["ba"])


a=5
b=3


#control statement 제어문
#먼저 기술한 명령이 먼저 실행된다.
#실행의 순서를 제어.
#선택문 : if, match~case
#반복문 : for, while (do~while없음)
#무시문 : break, continue
#복귀문 : return

#조건문
#money=int(input("현재 보유 금액 입력 :"))

#if money>=20000:
#    print("택시를 타고 가라")
#else:
#    print("걸어가라")

#print("Good night!!")

#조건문 2
#ent =10000
#age=int(input("나이 입력 :"))

#if age>=20:
#    ent = ent +ent*0.1

#print(f"입장료 = {ent}")

#조건문 3
#score = int(input("점수입력 : "))

#if score>=90:
#    print("A학점")
#elif score>=80:
#    print("B학점")
#elif score>=70:
#    print("C학점")
#elif score>=60:
#    print("D학점")
#else :
#    print("F학점")

#조건문 예제
#윤년은 4의 배수이고, 100의 배수는 아니고 400

year = int(input("연도 입력 : "))

if year % 4==0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}년은 윤년(leap year)입니다.")
else:
    print(f"{year}년은 평년(common year)입니다.")