def insert_string(s, k, n):
    insert_part = s[-n:]

    result = insert_part + k

    return result

s = input("첫 번째 문자열을 입력하세요: ")
k = input("두 번째 문자열을 입력하세요: ")
n = int(input("양의 정수를 입력하세요: "))

# 함수 호출하여 결과 출력
result = insert_string(s, k, n)
print("결과:", result)
