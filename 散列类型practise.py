'''
 数值类型:
整型（int）浮点型（float）布尔类型（bool）复数（complex）
 序列类型:
列表（list）字符串（string）元组（tuple）
 散列类型:
集合（set） 字典（dict）
可变：列表、字典、集合
不可变：数字、字符串、元组
 可迭代对象：序列类型 and 散列类型
'''

User = {'姓名': '孙悟空', '身高': 180, '年龄': 18}
User['性别'] = '男'
del User['身高']
User['姓名'] = '猪八戒'
print(User)

list1 = [1, 1, 12, 2, 2, 2, 2, 3, 3, 4, 45, 5, 5, 55]
print(list(set(list1)))

