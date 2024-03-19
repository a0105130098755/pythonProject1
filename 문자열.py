my_list = [5,5,2,5,1,8,9,4,7,5,4,8]

slice_without_step = my_list[2:7]
slice_with_step = my_list[1:8:3]
print(slice_without_step)
print(slice_with_step)
jumin = "990212-1496912"
print('성별: ' + jumin[7])
print("년: "+ jumin[:2])
print("월 : "+ jumin[2:4])
print("일 : "+jumin[4:6])
print("생년월일 : "+jumin[:6])
print("뒤 7자리 : "+ jumin[7:])
print("뒤 7자리 : "+jumin[-7:])

#python_str = "life is short, you need python"
#new_str = python_str[0] + python_str[3]
#print(new_str)

phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 돟은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장"))
print(phrase.index("포기"))
print(phrase.find("나에게"))

new_str = phrase.replace("가장", "나에게")

print("태양고"+"나희도")
print("태양고"*2)

input_a = """
    안녕하세요.
문자열 함수를 알아 봅니다.

    """
print(input_a.strip())