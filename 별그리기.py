import turtle

def draw_star(size):
    # 거북이 객체 생성
    t = turtle.Turtle()
    t.speed(1)  # 거북이의 그리는 속도 설정

    # 별 모양을 그리는 반복문
    for _ in range(5):
        t.forward(size)  # size만큼 전진
        t.right(144)  # 360도를 5등분하여 각 꼭지점에 대한 회전

    # 그림 창을 닫습니다.
    turtle.done()

# 별의 크기를 설정합니다.
star_size = 100
draw_star(star_size)
