def fibonacci_sequence(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    try:
        count = int(input("몇 개의 피보나치 수를 출력할까요? "))
    except ValueError:
        print("정수를 입력해 주세요.")
    else:
        if count <= 0:
            print("1 이상의 값을 입력해 주세요.")
        else:
            sequence = fibonacci_sequence(count)
            print("피보나치 수열:", sequence)
