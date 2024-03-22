def divide_numbers():
    try:
        # 사용자로부터 두 개의 숫자 입력 받기
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        # 나눗셈 수행
        result = num1 / num2
        print("나눗셈 결과:", result)

    except ValueError:
        # 사용자가 숫자가 아닌 값을 입력한 경우
        print("올바른 숫자를 입력하세요.")

    except ZeroDivisionError:
        # 두 번째 숫자가 0인 경우
        print("0으로 나눌 수 없습니다.")

    except Exception as e:
        # 그 외의 예외 처리
        print("오류 발생:", e)


# divide_numbers 함수 호출
divide_numbers()
