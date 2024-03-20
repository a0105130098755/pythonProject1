from datetime import datetime

curr_year = datetime.today().year
jumin = input("주민등록번호 : ")
year = int(jumin[:2])
gender = int(jumin[7])
month = int(jumin[2:4])
day = int(jumin[4:6])

# 성별과 연도 계산을 함께 처리
if gender in (1, 2):
    year += 1900
else:
    year += 2000

# 현재 연도를 기준으로 나이 계산
age = curr_year - year

# 성별 문자열 지정
gender_str = "남성" if gender in (1, 3) else "여성"

print(f"생년월일 : {year:02}년 {month:02}월 {day:02}일")
print(f"성별 : {gender_str}")
print(f"나이 : {age}")
