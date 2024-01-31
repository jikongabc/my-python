# 1
try:
    num1 = input('请输入第一个数字：')
    num2 = input('请输入第二个数字：')
    print(int(num1) / int(num2))
except ZeroDivisionError as e1:
    print('除零错误:' + str(e1))

# 2
try:
    file1 = input('请输入您想读取的文件：')
    with open(file1, 'r', encoding='utf-8') as f1:
        lines1 = f1.readlines()
        for line1 in lines1:
            print(line1)
except FileNotFoundError as e2:
    print('该文件不存在：' + str(e2))

# 3
try:
    file2 = input('请输入您想读取的文件：')
    with open(file2, 'r', encoding='utf-8') as f2:
        lines2 = f2.readlines()
        for line2 in lines2:
            print(int(line2))
except ValueError as e3:
    print('该文件中有字符串无法转换为整型：' + str(e3))
