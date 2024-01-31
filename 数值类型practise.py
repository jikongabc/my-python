info1 = '123Helo_World'
print(info1[0], end='\n'), (info1[3::1])

info2 = '123@456@789'

print(info2.split('@', ))
print(info2.count('@'))
print(info2.replace('@', ',', ))

name = input('请输入您的姓名:')
age = input('请输入您的年龄:')
height = input('请输入您的身高:')
print(f"My name is {name},I was {height}cm tall at the age of {age}.")

num1 = input('请输入第一个数字:')
num2 = input('请输入第二个数字:')
print(int(num1) + int(num2))
