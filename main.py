import os
import collections

from _collections import deque


"""

def func(num1):
    def number(num2=5):
        return num1*num2
    return number()

print(func(6))

"""
"""

# замыкание:
def func2(num1):
    def number2(num2):
        return num1*num2
    return number2

print(func(6)(3))
"""
calculator = lambda x, y=0: x+y

a, f = 2 , 6
print(calculator(a, f))

def func(num1, num2, num3=7):
    return num1+num2

print(func(1,2))
print(func(2,num3=0,num2=7))  # передача сначала позиционным методом, а потом по ключам (в другом порядке не поймет)

def fun3(*args):
    return sum(*args)

def fun4(*fun):  # то же, то рекомендуется использовать args для произвольного к-ва аргументов
    return sum(*fun)

def fun5(**kwargs):
    return print(**kwargs['num1'])

#print(fun5({'11', 4}))

print(locals())
print(globals())

# вывод строк из файла
with open("text.txt") as file:
    for num, string in enumerate(file.readlines()):
        print(str(num) + "===" + string)
print(os.listdir)

def generator(n):
    for n in range(n):
        yield num+1
        yield num*10
for x in generator(3):
    print (x)

# пример работы с декоратором (оборачивание замкнутой функции?)

def decorator(funx):
    def pretty_text(argum):
        print("Стартуем")
        a = funx(argum)
        return f"=={a}=="
    print("Оборачиваем")
    return pretty_text

@decorator #  наше имя декоратора, например @name(4), где 4 - условный пробрасываемый аргумент функции name
def word(text: str):
    print("Стартуем функцию")
    return  text

print(word("Yo-Ho-Ho!"))
print("Завершаем")

# ====
def decor(foo):
    def prettify():
        return f"=={foo()}=="
    return prettify

@decor
def text():
    return "text"

print(text())  # если хотим передать сюда текст, то должны выше передать аргумент вместо фуу - (а)

# ====
def decor(foo):
    def prettify(a):
        return f"=={a}=="
    return prettify

@decor
def text(a):
    return a

print(text('!!!!'))  # если хотим передать сюда текст, то должны выше передать аргумент вместо фуу - (а)
# декоратор - функция, получающая и передающая функцию в качестве аргумента, т.е. prettify

# ================================================================================================
# class 7 - CLASS ================================================================================

def empty ():
    pass # временная заглушка

print(empty())

class MyClass:
    pass

class Ball:

    shape = "круглый" # тут атрибуты класса ! к слову эти атрибуты не могут использоваться внутри методов класса

    def __init__(self): # функция, задающая атрибуты класса при его создании
        self.color = "Green"  # тут атрибуты объекта !
        self.size = 15

    def jump(self):
        return self.size * 3
        # return "High!"

b = Ball()
print(b.jump())
print(b.color)

Ball().shape = "квадратный"
Ball().color = "Red"

print(Ball().color, Ball.shape)

a = Ball()
print(a.shape)
Ball.shape = "треугольный"
b = Ball ()
print(a.shape, b.shape)
b.shape = "плоский"
print(a.shape, b.shape)
Ball.shape = "овальный"
print(a.shape, b.shape)

a2 = Ball()
print(a2.size)
Ball().size = 777
b2 = Ball()
b2.size = 4
print(a2.size, b2.size)

class BallNew:

    size0 = 5
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def jump(self, size2):
        return self.size * size2

    @classmethod
    def some_method(cls): # нужен, когда мы можем передать класс, но без обязательного указания аттрибута
        return "Some_Class"

    @staticmethod
    def fixed_method(): # нужен, когда мы можем передать класс, но без обязательного указания аттрибута
        return "Fix"

    def __call__(self):
        return f"Я {self.color} мяч!"


w = BallNew(color="Green", size=20)
w2 = BallNew("Blue", 11)

print(w.jump(10)) # атрибут метода!

#print(w.classmethod())

class BasketBall(BallNew):
    def __init_subclass__(cls, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return f"Я баскетбольный {self.size} см мяч!"

g = BasketBall("Black", 100)
print(g())

class Iterator:
    """Это простой итератор"""

    def __init__(self, start):
        self.data = start

    def __iter__(self):
        return self

    def __next__(self):
        i = self.data
        self.data += 1
        return i

d = Iterator(1).__doc__
a = Iterator(1)
print(d)
print(next(a))
print(next(a))
print(next(a))

def function(param1, param2):
    """Простая функция:
    : param1 : str
    : param2 : int
    """
    pass

function(1, 2).__doc__

request.get()
