def my_func(x, y):
    """Возвращает x в сетепени y, при этом y - целое отрицательное число"""
    res = 1
    for _ in range(-y):
        res /= x
    return res


first_number = float(input('Введите x: '))
second_number = int(input('Введите y: '))
print(f'{first_number} ^ {second_number} = {my_func(first_number, second_number)}')
