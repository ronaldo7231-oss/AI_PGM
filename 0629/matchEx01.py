#Ex01 성적평가 프로그램(점수를 입력하는 경우)
score = int(input("Enter your score : "))
oneDigit = score // 10
match oneDigit:
    case 10 | 9:
        print("Excellent!")
    case 8:
        print("Good job!")
    case 7:
        print("You can do better.")
    case 6:
        print("You need to work harder.")
    case _:
        print("You need to improve your performance")

print("Thank you for using the grade evaluator.")