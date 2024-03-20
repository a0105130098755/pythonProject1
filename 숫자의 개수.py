from collections import Counter
A, B, C = map(int, input("정수 3개 입력 : ").split())
result = str(A * B * C)
counts = Counter(result)
for i in range(10):
    print(counts[str(i)])
