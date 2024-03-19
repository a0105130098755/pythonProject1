name = "고명규"
age = 25
gender = "남성"
jobs = "소프트웨어 개발자"
addr = "전라북도 익산시"

# C언어 스타일, %방식
print("====== C 스타일 ======")
print("이름 : %s"%(name))
print("나이 : %d"%(age))
print("성별 : %s"%(gender))
print("직업 : %s"%(jobs))
print("주소 : %s\n"%(addr))

print("====== 파이썬 스타일 2 ======")
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender}")
print(f"직업 : {jobs}")
print(f"주소 : {addr}\n")

# 자바 스타일
print("====== 자바 스타일 ======")
print("이름 : " + name)
print("나이 : " + str(age))
print("성별 : " + gender)
print("직업 : " + jobs)
print("주소 : " + addr)

#정렬
print(f"|{10:5}|")  # 오른쪽 정렬, 10이라는 값을 오른쪽 정렬으로 출력 한다는 의미
print(f"|{10:<5}|") # 왼쪽 정렬, 10이라는 값을 왼쪽 정렬으로 출력 한다는 의미
print(f"|{10:^6}|") # 중간 정렬, 10이라는 값을 중간 정렬 한다는 의미
print(f"{20.3333333:.2f}")