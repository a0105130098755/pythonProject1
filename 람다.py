def outer_function():
    outer_variable = "Outer Variable"

    # 람다 함수를 이용하여 inner_function 정의
    inner_function = lambda: print("Inner function:", outer_variable)

    # inner_function 호출
    inner_function()
    # outer_function 내부에서의 변수에 접근
    print("Outer function:", outer_variable)

# outer_function 호출
outer_function()
