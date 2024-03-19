# num = int(input("정수를 입력 하세요"))
# if num > 100:
#     print("입력 값이 100보다 커요")
# elif num <100:
#     print("입력 값이 100보다 작아요")
# else:
#     print("100입니다")

# season = input("지금 계절은 ? ")
# if season == "spring":
#     print("따뜻한 봄이 왔어요")
# elif season == "summer":
#     print("무더운 여름 입니다")
# elif season == "fall" or season == "autumn":
#     print("쓸쓸한 가을 입니다")
# else:
#     print("추운 겨울 입니다")

math_score = int(input("수학 점수를 입력하세요: "))
korean_score = int(input("국어 점수를 입력하세요: "))
english_score = int(input("영어 점수를 입력하세요: "))

average_score = (math_score + korean_score + english_score) / 3

if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"수학: {math_score}, 국어: {korean_score}, 영어: {english_score}")
print(f"평균 성적: {average_score:.2f}, 학점: {grade}")
