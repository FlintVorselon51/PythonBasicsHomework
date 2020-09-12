def division(a, b):
    """Возвращает частное от деления."""
    return a / b


first_number = float(input('Введите числитель: '))
second_number = float(input('Введите знаменатель: '))
try:
    print(f'{first_number} / {second_number} = {division(first_number, second_number)}')
except ZeroDivisionError:
    print('Ошибка! Деление на ноль!')
