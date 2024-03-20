def print_multiplication_table():
    for i in range(1, 10):
        print(f"{i}단을 출력합니다:")
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print()  # 한 단의 출력이 끝나면 빈 줄을 출력하여 단을 구분합니다.

def main():
    print_multiplication_table()

if __name__ == "__main__":
    main()
