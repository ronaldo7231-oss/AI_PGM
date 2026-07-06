while True:
    print("\n=== CLI 계산기 ===")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 종료")

    choice = input("선택: ")

    if choice == "5":
        print("종료합니다.")
        break

    a = float(input("첫 번째 숫자: "))
    b = float(input("두 번째 숫자: "))

    if choice == "1":
        print("결과:", a + b)
    elif choice == "2":
        print("결과:", a - b)
    elif choice == "3":
        print("결과:", a * b)
    elif choice == "4":
        if b == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            print("결과:", a / b)
    else:
        print("잘못된 선택입니다.")