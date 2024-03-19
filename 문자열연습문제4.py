# 사용자로부터 여러 개의 정수를 입력 받아 합계와 평균을 구합니다.
numbers = [int(num) for num in input("여러 개의 정수를 입력하세요 (쉼표로 구분하여): ").split(',')]
total, count = sum(numbers), len(numbers)
print("합계:", total, "\n평균:", total / count)
