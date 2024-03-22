class MovieBookingSystem:
    def __init__(self, num_seats):
        self.num_seats = num_seats
        self.available_seats = set(range(num_seats))
        self.total_sales = 0

    def book_seat(self, seat_index):
        if seat_index not in self.available_seats:
            print("이미 예매된 좌석 이거나 잘못된 좌석 번호 입니다.")
            return

        self.available_seats.remove(seat_index)
        self.total_sales += 12000
        print(f"좌석 {seat_index} 예매가 완료 되었습니다.")

    def cancel_booking(self, seat_index):
        if seat_index in self.available_seats:
            print("이미 빈 좌석 입니다.")
            return

        self.available_seats.add(seat_index)
        self.total_sales -= 12000
        print(f"좌석 {seat_index} 예매가 취소 되었습니다.")

    def display_total_sales(self):
        print(f"총 매출액: {self.total_sales}원")

def main():
    num_seats = 10  # 좌석 수
    movie_system = MovieBookingSystem(num_seats)

    while True:
        print("===== 영화 예매 시스템 =====")
        print("1. 좌석 예매")
        print("2. 좌석 취소")
        print("3. 종료")

        choice = input("선택: ")

        if choice == '1':
            seat_index = int(input("예매할 좌석 번호를 입력 하세요: "))
            movie_system.book_seat(seat_index)
        elif choice == '2':
            seat_index = int(input("취소할 좌석 번호를 입력 하세요: "))
            movie_system.cancel_booking(seat_index)
        elif choice == '3':
            movie_system.display_total_sales()
            print("프로그램을 종료 합니다.")
            break
        else:
            print("잘못된 입력 입니다. 다시 입력 해주세요.")

if __name__ == "__main__":
    main()
