# key1(打印1到10)
for i1 in range(1, 11):
    print(i1)

# key2(1到100累加)
# 方案1(0,1)
count1 = 0
count2 = 1
while count2 <= 100:
    count1 += count2
    count2 += 1
print(count1)

# 方案1(1,1)
count3 = 1
count4 = 1
while count3 <= 99:
    count3 += 1
    count4 += count3
print(count4)

# 方案2
list1 = [x1 for x1 in range(1, 101)]
print(sum(list1))

# key3(1到100偶数累加)
# 方案1(0,2)
count5 = 0
count6 = 2
while count6 <= 100:
    count5 += count6
    count6 += 2
print(count5)

# 方案1(2,2)
count7 = 2
count8 = 2
while count7 <= 98:
    count7 += 2
    count8 += count7
print(count8)

# 方案2
list2 = [x2 * 2 for x2 in range(1, 51)]
print(sum(list2))

# key4(猜年龄)
key_age = 25
for i2 in range(3):
    age = input("请输入您猜测的年龄：")
    if int(age) == key_age:
        print("恭喜您猜对了！")
        break
    else:
        continue
