# 1.False 2.报错 3.False 4.True

# 程序1
age = int(input('请输入您的年龄:'))
if age >= 18:
    print("可以申请驾驶执照")
else:
    print("不能申请驾驶执照")

# 程序2
score = int(input('请输入您的成绩:'))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")

# 程序3
year = int(input('请输入您想查询的年份:'))
if year % 4 == 0 and year % 4 != 100 or year % 400 == 0:
    print("是闰年")
else:
    print("不是闰年")

# 程序4
month = int(input('请输入您想查询的月份:'))
if month in {3, 4, 5}:
    print("春")
if month in {6, 7, 8}:
    print("夏")
if month in {9, 10, 11}:
    print("秋")
if month in {12, 1, 2}:
    print("冬")
