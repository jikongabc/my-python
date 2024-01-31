# key1
def calculate_average(*args):
    return sum(args) / len(args)


a = calculate_average(520, 1314)
print(a)


# key2
def reverse_string(x):  # x是字符串
    return x[::-1]


b = reverse_string("hello_word")
print(b)


# key3
def count_words(y):  # y是字符串
    return len(y.split())


c = count_words("hello word")
print(c)


# key4
def is_even(z):  # z是整数
    if z % 2 == 0:
        return True
    else:
        return False


d = is_even(2)
print(d)


# key5
def find_max(m):  # m是列表
    return max(m)


e = find_max([520, 1314])
print(e)
