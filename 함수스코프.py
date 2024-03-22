def outer_function():
    # outer_function 내부에서의 변수 정의
    outer_variable = "Outer Variable"

    def inner_function():
        # inner_function 내부에서의 변수 정의
        inner_variable = "Inner Variable"
        print("Inner function:", inner_variable)
        # outer_function의 변수에 접근 가능
        print("Inner function accessing outer variable:", outer_variable)

    # inner_function 호출
    inner_function()
    # outer_function 내부에서의 변수에 접근
    print("Outer function:", outer_variable)
    # inner_function에서 정의된 변수는 접근할 수 없음
    # print("Outer function accessing inner variable:", inner_variable)  # 에러 발생!

# outer_function 호출
outer_function()
