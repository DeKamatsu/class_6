import os

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