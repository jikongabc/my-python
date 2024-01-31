a = map(lambda x1: x1 ** 2, range(1, 6))
print(list(a))

b = filter(lambda x2: x2 % 2 == 0, range(1, 6))
print(list(b))

c = sorted(['ccc', 'a', 'aa', 'bbbb'], key=len)
print(list(c))
