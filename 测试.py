# Chinese = int(input('请输入您的语文成绩：'))
# Math = int(input('请输入您的数学成绩：'))
# English = int(input('请输入您的英语成绩：'))
# score = Chinese + Math + English
# print(score)
# if score >= 270:
#     print('优秀')
# elif score >= 240:
#     print('良好')
# elif score >= 180:
#     print('合格')
# else:
#     print('不合格')


layer = int(input('请输入打印的奇数行数：'))
while layer % 2 == 0:
    layer = int(input('必须是奇数，请重新输入打印的行数：'))

for i in range(1, (layer // 2 + 2)):
    num1 = layer // 2 + 1 - i
    for j in range(num1):
        print(' ', end='')
    num2 = i * 2 - 1
    for k in range(num2):
        print('*', end='')
    print('')

for i in range((layer // 2), 0, -1):
    num1 = layer // 2 + 1 - i
    for m in range(num1):
        print(' ', end='')
    num2 = 2 * i - 1
    for n in range(num2):
        print('*', end='')
    print('')


# class Human:
#     def __init__(self, height, weight):
#         self.height = height
#         self.weight = weight
#
#     def BMI(self):
#         bmi = self.weight / self.height ** 2
#         print(f"bmi为{bmi}")
#         if bmi < 18.5:
#             print('过轻')
#         elif bmi < 24:
#             print('正常')
#         elif bmi < 28:
#             print('过重')
#         elif bmi < 32:
#             print('肥胖')
#         else:
#             print('非常肥胖')
#
#
# height = float(input('请输入您的身高(m)：'))
# weight = float(input('请输入您的体重(kg)：'))
# a = Human(height, weight)
# a.BMI()

