lines = int(input())
factorial = 1
temporary = 0
for _ in range(lines):
    factorial = 1
    temporary = int(input())

    for i in range(2, temporary + 1):
        factorial *= i

    print(factorial)
