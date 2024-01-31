# 1
file_name1 = input('请输入您想写入的文件的名称：')
file_name1 = file_name1 + '.txt'
with open(file_name1, 'w', encoding='utf-8') as f1:
    f1.write(input('请输入您想写入文件的内容：'))
# 2
file_name2 = input('请输入您想读取的文件的名称：')
file_name2 = file_name2 + '.txt'
with open(file_name2, 'r', encoding='utf-8') as f2:
    print(f2.read())
# 3
file_name3 = input('请输入您想写入的第一个文件的名称：')
file_name4 = input('请输入您想写入的第二个文件的名称：')
file_name3 = file_name3 + '.txt'
file_name4 = file_name4 + '.txt'
with open(file_name3, 'r', encoding='utf-8') as f3:
    with open(file_name4, 'a', encoding='utf-8') as f4:
        f4.write(f3.read())

# 4
file_name5 = input('请输入您想查询的文件的名称：')
file_name5 = file_name5 + '.txt'
with open(file_name5, 'r', encoding='utf-8') as f5:
    content = f5.read()
print(content.count(input('请输入您想查询的字符：')))

