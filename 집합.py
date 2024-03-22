s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

# 중복 제거
s3 = set([1,2,3,4,5,6,2,3,4,5])
print(s3)

# 교집합
print(s1.intersection(s2))
(s1 & s2)

# 합집합
print(s1.union(s2))
print(s1 | s2)

# 차집합
print(s1.difference(s2))
print(s1 - s2)

