def search_list(a, x):
    try:
        return a.index(x)
    except ValueError:
        return -1

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 33))
print(search_list(v, 18))
print(search_list(v, 900))
