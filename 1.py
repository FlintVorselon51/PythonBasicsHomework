from sys import argv
try:
    production, rate, award = map(int, argv[1:])
    print(f'Заработная плата сотрудника - {production * rate + award}')
except ValueError:
    print('Нужно передать три параметра (Выработка, ставка и премия).')
