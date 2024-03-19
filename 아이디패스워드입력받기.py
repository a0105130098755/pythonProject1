
user = input("아이디 입력 :")
if len(user) >= 10:
    pw = input("비밀번호 입력 : ")
    if pw.__len__() < 8 or pw.__len__() > 16:
        print("비밀번호는 8자에서 16자 사이여야합니다")
    elif pw.find(user) >= 0:  # 없으면 -1을 반환 합니다.
        print("비밀번호에 아이디를 포함시킬 수 없습니다")
    else:
        print("아이디 : {}".format(user))
        print("비밀번호 : {}".format(pw))
else:
    print("아이디는 반드시 10자리 이상이여야합니다")