#name = input("이름을 입력하세요: ")
#print(name)
#kor = int(input("국어 성적 입력: "))
#print(f"국어 : {kor}")
kor, eng, mat = map(int,input("국어 영어 수학: ").split())
print(f"국어 : {kor}, 영어 : {eng}, 수학 : {mat}")

name, addr = input("이름과 주소 입력: ").split()

str1, str2 = input("이름과 주소 입력 : ").split()
print(str1,str2)

kor, eng, mat = map(int, input("국어 영어 수학 : ").split())
print(kor,eng,mat)

hour, min, sec = input("시:분:초 : ").split(":")
print(f"{hour}시{min}분{sec}초")

a,b,c = map(int, input("정수 입력 : ").split(":"))
if a > 12:
    a -= 12
    print(f"오후{a:02}시{b:02}분{c:02}초")
else:
    print(f"오전{a:02}시{b:02}분{c:02}초")