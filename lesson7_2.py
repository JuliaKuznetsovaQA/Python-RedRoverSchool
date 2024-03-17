a = '1'
b = 'hello'
try:
    print(a + b)
except (TypeError, ValueError):
    print('Ошибка')
else:
    print('Нет ошибки')
finally:
    print('Блок, который выполняется всегда')