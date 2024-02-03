a = int(input())
operator = input()
b = int(input())
result = None
if operator in ('+', '-', '/', '*', '//', '%'):
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '/':
        if b != 0:
            result = a / b
        else:
            print('Делить на ноль нельзя')
    elif operator == '*':
        result = a * b
    elif operator == '//':
        result = a // b
    elif operator == '%':
        result = a % b
    print(result)

else:
    print('Неверный знак операции')

