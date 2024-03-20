def get_input(prompt, valid_values):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() in valid_values:
            return user_input.lower()

def main():
    name = input("아름을 입력 하세요: ")
    age = int(input("나이를 입력 하세요 (1 ~ 199): "))
    gender = get_input("성별을 입력 하세요 (M/m: 남성, F/f: 여성): ", ['m', 'f'])
    occupation = int(input("직업을 입력 하세요 (1: 학생, 2: 회사원, 3: 주부, 4: 무직): "))

    print("\n===== 회원 정보 =====")
    print(f"이름: {name}")
    print(f"나이: {age}세")
    print(f"성별: {'남성' if gender == 'm' else '여성'}")
    print("직업:", end=" ")
    if occupation == 1:
        print("학생")
    elif occupation == 2:
        print("회사원")
    elif occupation == 3:
        print("주부")
    else:
        print("무직")

if __name__ == "__main__":
    main()
