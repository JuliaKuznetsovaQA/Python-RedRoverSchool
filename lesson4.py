"""4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую
3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата."""


# def square(a):
#     x = (4 * a, a * a, round(((2 * a * a) ** 0.5), 2))
#     print(x)
#
#
# square(3)

"""4.2. Напишите фукнцию, которая принимает произвольное количество именованных аргументов и выводит их построчно
     в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35
	position: web developer"""


# def pd(**kwargs):
#     for i in kwargs:
#         print(f'{i}: {kwargs[i]}')
#
#
# pd(name='John', last_name='Smith', age=35, position='web developer')


"""4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, 
содержащий только положительные числа"""

my_list = [20, -3, 15, 2, -1, -21]
new_list = list(filter(lambda x: x > 0, my_list))
print(new_list)

"""4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)"""

from functools import reduce

my_l = [20, -3, 15, 2, -1, -21]
res = reduce(lambda x, y: x * y, my_l)
print(res)

"""4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра """

import time

#
# def decorator_function(func):
#     def wrapper(*arg):
#         start_time = time.time()
#         func(*arg)
#         end_time = time.time()
#         result_time = end_time - start_time
#         print(result_time)
#         print()
#     return wrapper
#
# @decorator_function
# def square(a):
#     x = (4 * a, a * a, round(((2 * a * a) ** 0.5), 2))
#     print(x)
#
#
# square(3)
#
# import time
#
#
def time_decor(func):
    def wrapper(*arg):
        start_time = time.time()
        print(f'Работает функция {func.__name__}')
        func(*arg)
        end_time = time.time()
        result_time = end_time - start_time
        print(f'Время работы функции составило: {result_time}')
        print()
    return wrapper
#
#
# @time_decor
# def prime_factors_new(n):
#     res = ''
#     i = 2
#     while n > 1:
#         if n % i != 0:
#             i += 1
#             continue
#         else:
#             count = 1
#             n = n // i
#             while n % i == 0:
#                 n = n // i
#                 count += 1
#             if count > 1:
#                 res += f'({i}**{count})'
#             elif count == 1:
#                 res += f'({i})'
#             elif count == 0:
#                 continue
#             i += 1
#     if res == '':
#         res += f'({n})'
#     print(res)
#
#
# @time_decor
# def prime_factors_old(n):
#     res = ''
#     for i in range(2, (n//2) + 1):
#         count = 0
#         while n % i == 0:
#             n = n / i
#             count += 1
#         if count > 1:
#             res += f'({i}**{count})'
#         elif count == 1:
#             res += f'({i})'
#         elif count == 0:
#             continue
#     if res == '':
#         res += f'({n})'
#     print(res)
#
#
# prime_factors_old(7775460)
# prime_factors_new(7775460)
# prime_factors_old(7919)
# prime_factors_new(7919)


"""сколько мне лет"""
# import datetime
#
#
# @time_decor
# def age(year):
#     current_date = datetime.date.today()
#     current_age = current_date.year - year
#     print(current_age)
#
# age(1973)

"""4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, 
выполняющие базовые арифметические вычисления. 
     Примените эти функции в качестве методов в другом файле."""

# from my_calc import *
#
# divide_it(8, 4)
# minus_it(6, 3)
# power_it(7, 8)
# sum_it(100, 89)
# print(cube(5))
# print(sqrt(25))