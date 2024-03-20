def print_matrix(n):
    for i in range(1, n*n+1): print(f"{i:3}", end='\n' if i%n==0 else ' ')

try:
    n = int(input("정수값을 입력하세요: "))
    print_matrix(n)
except ValueError:
    print("올바른 숫자를 입력하세요.")
var = ()