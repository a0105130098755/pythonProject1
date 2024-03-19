url = input("사이트 : ")

my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")] # 슬라이싱, 처음부터 . 위치 미만까지
password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "jks"
print("비밀번호 : " + password)# 각 사이트 비밀번호 자동으로 만들기