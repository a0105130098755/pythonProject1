class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 덧셈 연산자 오버로딩
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

# Point 객체 생성
p1 = Point(1, 2)
p2 = Point(3, 4)

# 덧셈 연산자 사용
result = p1 + p2

# 결과 출력
print(result)  # (4, 6)
