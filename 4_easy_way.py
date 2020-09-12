def my_func(x, y):
    """Возвращает x в степени y."""
    return x**y


first_number = float(input('Введите x: '))
second_number = int(input('Введите y: '))
print(f'{first_number} ^ {second_number} = {my_func(first_number, second_number)}')
