"""4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции,
выполняющие базовые арифметические вычисления.
     Примените эти функции в качестве методов в другом файле."""


def sum_it(a, b):
    print(a + b)


def power_it(a, b):
    print(a * b)


def minus_it(a, b):
    print(a - b)


cube = lambda a: a ** 3
sqrt = lambda a: a ** 0.5


def divide_it(a, b):
    print(a / b)