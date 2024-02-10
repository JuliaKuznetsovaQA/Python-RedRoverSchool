
"""3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3"""

# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2][0], my_list[2][1], my_list[2][2])

"""3.2 Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'"""

# list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
# total = 0
# for i in list_1:
#     if type(i) is int:
#         total += i
#     else:
#         continue
# print(total)
#
# list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
# total = 0
# for i in list_1:
#     if type(i) is str and 'a' in i:
#         print(i)
#     else:
#         continue


"""3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж"""

# l = ['cat', 'dog', 'horse', 'cow']
# print(tuple(l))

"""3.4. Напишите программу, которая определяет, какая семья больше.
      1) Программа имеет два input() - например, family_1, family_2.
      2) Членов семьи нужно перечислить через запятую.
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')"""

# family_1 = input("Перечислите членов семьи через запятую:").split(',')
# family_2 = input("Перечислите членов семьи через запятую:").split(',')
# if len(family_1) == len(family_2):
#     print("Equal")
# elif len(family_1) > len(family_2):
#     print(','.join(family_1))
# else:
#     print(','.join(family_2))


"""3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. 
В значения можете передать информацию
    о вашем любимом фильме.
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение"""

# film = {'title': 'Kill Bill', 'director': 'Tarantino', 'year': 2004, 'budget': 10000000,
#         'main_actor': 'Uma Turman', 'slogan': 'Revenge is a dish best served cold'}
# print(film.keys())
# print(film.values())
# print(film.items())

"""3.6. Найдите сумму всех значений в словаре 
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}"""

# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))

"""3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]"""

# l = [1, 2, 3, 4, 5, 3, 2, 1]
# n = []
# for i in range(len(l)):
#     if l[i] not in n:
#         n.append(l[i])
#     else:
#         continue
# print(n)

"""3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, 
                            set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     # - проверьте являются ли эти множества подмножествами друг друга"""

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1 & set2)
print(set1.intersection(set2))
print(set1 - (set1 & set2) | set2 - (set1 & set2))
print(set1.symmetric_difference(set2))