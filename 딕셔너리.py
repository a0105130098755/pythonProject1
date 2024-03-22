dict = {"정경수":90, "고유림":88, "나희도":89}
print(dict.keys())
print(dict.values())
print(dict.items())
print("고유림" in dict)
print("안유진" in dict)

if "고유림" in  dict:
    print(dict["고유림"])
