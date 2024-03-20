word = input("단어 입력 : ")
print(''.join([c.lower() if c.isupper() else c.upper() for c in word]))
