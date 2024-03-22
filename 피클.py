import pickle

# 저장할 데이터(파이썬 객체) 정의
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# 객체를 파일에 피클링하여 저장
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# 파일에서 피클링된 데이터를 읽어와 역직렬화하여 객체로 로드
with open('data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)

# 로드된 데이터 출력
print(loaded_data)
