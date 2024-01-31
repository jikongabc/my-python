# key_age = 25
# for i in range(3):
#     age = input("请输入您猜测的年龄：")
#     if int(age) == key_age:
#         print("恭喜您猜对了！")
#         break
#     else:
#         continue


# key_age = 25
# for i in range(3):
#     age = input("请输入您猜测的年龄：")
#     if age == str(key_age):
#         print("恭喜您猜对了！")
#     else:
#         if i <= 1:
#             print(f"您猜错了，还有{2 - i}次机会")
#         else:
#             print("程序已锁死")


key_age = 25


def age_guess():
    for i in range(3):
        age = input("请输入您猜测的年龄:")
        if age.isdigit():
            if int(age) == key_age:
                print("恭喜您猜对了")
                break
            else:
                if i <= 1:
                    print(f"您猜错了,还有{2 - i}次机会")
                else:
                    print("程序已锁死")
        else:
            print("您输入的有误,请重新输入")
            return age_guess()


age_guess()
