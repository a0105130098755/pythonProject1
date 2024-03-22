def rejected_guests(n, seats):
    occupied = {}  # 이미 앉아있는 손님의 자리를 저장할 딕셔너리
    rejected_count = 0  # 거절당한 손님의 수

    for seat in seats:
        if seat in occupied:  # 자리가 이미 차있으면 거절당함
            rejected_count += 1
        else:
            occupied[seat] = True  # 자리를 차지함

    return rejected_count

N = int(input())  # 손님의 수
seats = list(map(int, input().split()))  # 손님이 앉고 싶어하는 자리 번호 리스트

print(rejected_guests(N, seats))
