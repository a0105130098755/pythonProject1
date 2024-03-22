numbers = list(map(int, input("수를 공백을 기준 으로 정수를 입력 하세요: ").split()))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("홀수:", odd_numbers, "\n짝수:", even_numbers)
