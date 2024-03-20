def print_star_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j <= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def main():
    try:
        num = int(input("별의 개수를 입력하세요: "))
        print_star_pattern(num)
    except ValueError:
        print("올바른 숫자를 입력하세요.")

if __name__ == "__main__":
    main()
