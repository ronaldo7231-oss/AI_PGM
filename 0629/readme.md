assignment(대입, 할당 : 우측 수식의 연산 결과를 왼쪽의 변수에 대입)
variable =	expression
		literal or constant	a = 1
		variable			a = b
		operator			a = b + 1
		function			a = sum(1,2) * a + 1
		fubction의 구성요소 (variable, literal, operator, function)

산술연산자
< ,<= ,> ,>= ,== ,!= ,in ,not ,is ,is not 관계연산자
비트연산자
not, and, or 논리연산자

--------------------------------------------------
if ():
	print("")	<- 파이썬에서 이게 없으면 error가 뜬다. 그걸 방지하기 위해서 
else :
	print("")

if ():
	pass		<- 이걸 사용한다.
else :
	print("")
--------------------------------------------------
if 형태 3가지
1. if
2. if ~ else
3. if ~ elif ~ elif ~ .... ~ else
--------------------------------------------------
match 수식:
    case 값1:
        수행할_문장1
        ...
    case 값2:
        수행할_문장2
        ...
    case _:
        수행할_문장3
        ...
--------------------------------------------------
제어문
선택문 : if, match~case 
반복문 : for, while
무시문 : break, continue
복귀문 : return
--------------------------------------------------
프로그래밍 에러
1. syntax(구문) error
2. run time error(exception)
3. semantic error
--------------------------------------------------
range(start:stop:step)
--------------------------------------------------
함수 = 변수 + 명령

시스템 : 특정한 목적을 위하여 여러 구성 요소가 상호작용하는 유기적인 집합체

파일의 구성요소 두가지
1. 파일에 대한 정보(파일이름, 확장자, 파일 소유자, 파일 생성 일시, etc)
2. 파일 내용
