number = int(input("Enter a number: "))

for i in range(1, number +1):
    for j in range(number -i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()
    