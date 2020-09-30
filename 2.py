class DivisionByZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


print('Операция деления.')
a = int(input('Введите числитель: '))
b = int(input('Введите знаменатель: '))

try:
    if b == 0:
        raise DivisionByZeroError('Деление невозможно! Знаменатель равен нулю!')
except DivisionByZeroError as error:
    print(error)
else:
    print(f'{a} / {b} = {round(a / b, 3)}')
finally:
    print('Работа программы завершена.')
