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

fruits=[]
fruit = input("Enter a fruit: ")
fruits.append(fruit)
fruit = input("Enter a fruit: ")
fruits.append(fruit)
fruit = input("Enter a fruit: ")
fruits.append(fruit)
fruit = input("Enter a fruit: ")
fruits.append(fruit)
fruit = input("Enter a fruit: ")
fruits.append(fruit)
print(fruits)
print(fruits[0])
print(fruits[-1])