# 데코레이터 함수 정의
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # 데코레이팅된 함수 호출
        print("Something is happening after the function is called.")
    return wrapper

# 데코레이터를 사용하여 기능을 추가할 함수 정의
@my_decorator
def say_hello():
    print("Hello!")

# 함수 호출
say_hello()
