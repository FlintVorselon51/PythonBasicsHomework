print('Простой калькулятор.')
print('Выберите операцию. Для этого введите:')
print('0. Для того, чтобы выйти из программы')
print('1. Сложить два числа (a + b)')
print('2. Вычислить разность двух чисел (a - b)')
print('3. Перемножить два числа (a * b)')
print('4. Поделить два числа (a / b)')
print('5. Возвести число в степень (a ^ b)')
print('6. Найти остаток от деления на число (a % b)')
print('7. Найти результат целочисленного деления (a // b)')

symbol = ''
result = 0

while True:
    choice = int(input())
    if choice == 0:
        break
    if 0 < choice < 8:
        a = float(input('Введите a: '))
        b = float(input('Введите b: '))
    if choice == 1:
        symbol = '+'
        result = a + b
    elif choice == 2:
        symbol = '-'
        result = a - b
    elif choice == 3:
        symbol = '*'
        result = a * b
    elif choice == 4:
        symbol = '/'
        result = a / b
    elif choice == 5:
        symbol = '^'
        result = a ** b
    elif choice == 6:
        symbol = '%'
        result = a % b
    elif choice == 7:
        symbol = '//'
        result = a // b
    if 0 < choice < 8:
        print(f'{a} {symbol} {b} = {result:.3f}')
    print('Пожалуйста, введите число от 1 до 7')
