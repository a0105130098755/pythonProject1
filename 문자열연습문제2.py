from datetime import datetime
curr_year = datetime.today().year
jumin = input("주민등록번호 : ")
year = int(jumin[:2])
gender = int(jumin[7])
month = int(jumin[2:4])
day = int(jumin[4:6])

if gender == 1 or gender == 2:
    age = curr_year - 1900 - year
else:
    age = curr_year - 2000 - year

if gender == 1 or gender == 3:
    gender_str = "남성"
else:
    gender_str = "여성"

print(f"생년월일 : {year:02}년 {month:02}월 {day:02}일")
print(f"성별 : {gender_str}")
print(f"나이 : {age}")