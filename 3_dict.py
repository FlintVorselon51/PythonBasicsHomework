numbers_and_months = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}

seasons_and_numbers = {
    'Зимы': (1, 2, 12),
    'Весны': (3, 4, 5),
    'Лета': (6, 7, 8),
    'Осени': (9, 10, 11)
}

while True:
    print('Введите 0, если хотите выйти')
    n = int(input('Введите номер месяца: '))
    if n == 0:
        break
    print(f'{n}-й месяц это {numbers_and_months[n]}' if 0 < n < 13 else 'Пожалуйста введите число от 1 до 12')
    for key in seasons_and_numbers.keys():
        print(f'{numbers_and_months[n]} это месяц {key}' if n in seasons_and_numbers[key] else '', end='')
    print()
