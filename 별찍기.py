n = int(input("정수를 입력 하세요: "))
for i in range(n, 0, 1):
    print(" " * (n - i) + "*" * i)
