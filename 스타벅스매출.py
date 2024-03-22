file_name = "스타벅스일일매출.txt"


f = open(file_name)                 # 파일 읽기
header = f.readline()               # 데이터의 첫 번째 줄을 읽음
header_list = header.split()        # 첫 줄의 문자열을 분리한 후 리스트로 변환

espresso = []
americano = []
cafelatte = []
cappucino = []

for line in f :                     # 두 번째 줄부터 데이터를 읽어서 반복 처리
    data_list = line.split()        # 문자열으 분리해서 리스트로 변환
    # 커피 종류별로 정수로 변환한 후, 리스트의 항목으로 추가
    espresso.append(int(data_list[1]))
    americano.append(int(data_list[2]))
    cafelatte.append(int(data_list[3]))
    cappucino.append(int(data_list[4]))

f.close()                           # 파일 닫기

print(f"{header_list[1]} 전체 판매량 : {sum(espresso)}, 일 평균 판매량 : {sum(espresso)/len(espresso)}")
print(f"{header_list[2]} 전체 판매량 : {sum(americano)}, 일 평균 판매량 : {sum(americano)/len(americano)}")
print(f"{header_list[3]} 전체 판매량 : {sum(cafelatte)}, 일 평균 판매량 : {sum(cafelatte)/len(cafelatte)}")
print(f"{header_list[4]} 전체 판매량 : {sum(cappucino)}, 일 평균 판매량 : {sum(cappucino)/len(cappucino)}")