# answer1
class Person:
    def __init__(self, name1):
        self.name1 = name1

    def introduce(self):
        print(f'我的名字是{self.name1}')


class Student(Person):
    def study(self):
        print('我可以学')


class Teather(Person):
    def teath(self):
        print('我可以教')


a1 = Student('寂空1')
b1 = Teather('寂空2')
a1.introduce()
a1.study()
b1.introduce()
b1.teath()


# answer2
class Animal:
    def __init__(self, name2):
        self.name2 = name2

    def speak(self):
        if self.name2 == '狗':
            print('汪汪汪')
        elif self.name2 == '猫':
            print('喵喵喵')
        else:
            print('只能识别狗和猫')


class Dog(Animal):
    def bark(self):
        print('汪汪汪')


class Cat(Animal):
    def meow(self):
        print('喵喵喵')


a2 = Dog('狗')
b2 = Cat('猫')
a2.speak()
a2.bark()
b2.speak()
b2.meow()


# answer3
class Singleton:
    _instance = None
    _name = True

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            return cls._instance
        return cls._instance

    def __init__(self):
        if self._name:
            self.name = '寂空'


p1 = Singleton()
p2 = Singleton()
print(p1)
print(p2)
print(p1.name)
print(p2.name)


# answer4
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def describe_car(self):
        print(f'这是一辆{self.color}的{self.brand}')


car1 = Car('奔驰', '黑色')
car2 = Car('宝马', '白色')

print(car1.brand)
print(car1.color)
print(car2.brand)
print(car2.color)
car1.describe_car()
car2.describe_car()
