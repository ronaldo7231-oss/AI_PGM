number = int(input("Enter a number: "))

# 위쪽 피라미드
for i in range(1, number + 1):
    # 공백 출력
    for j in range(number - i):
        print(" ", end="")

    # 별 출력
    for j in range(2 * i - 1):
        print("*", end="")

    print()

# 아래쪽 역피라미드
for i in range(number - 1, 0, -1):
    # 공백 출력
    for j in range(number - i):
        print(" ", end="")

    # 별 출력
    for j in range(2 * i - 1):
        print("*", end="")

    print()