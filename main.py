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