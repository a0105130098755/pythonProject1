def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

# 가변 매개변수를 사용하여 합을 계산
result = calculate_sum(1, 2, 3, 4, 5)
print("결과:", result)
