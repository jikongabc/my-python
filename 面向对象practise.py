class Person:
    name = input('请输入您的名字：')
    age = input('请输入您的年龄：')


Person1 = Person()
print(f'姓名为：{Person1.name}')
print(f'年龄为：{Person1.age}岁')


class Rectangle:
    width = input('请输入宽：')
    height = input('请输入高：')

    def area(self):
        print(f'面积为；{int(self.width) * int(self.height)}')


Rectangle1 = Rectangle()
Rectangle1.area()


class BankAccount:
    balance = 100000000

    def deposit(self, money1):
        self.balance += int(money1)

        print(f'存款成功，您现在的余额为{self.balance}元')

    def withdrawal(self, money2):
        self.balance -= int(money2)
        print(f'取款成功，您现在的余额为{self.balance}元')


BankAccount1 = BankAccount()
answer = input('您想存款还是取款？（0/1）：')
if int(answer) is 0:
    BankAccount1.deposit(input('请输入您想存入的金额：'))
else:
    BankAccount1.withdrawal(input('请输入您想取出的金额：'))
