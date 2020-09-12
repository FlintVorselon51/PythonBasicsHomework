s = 0
end = False
print('Введите "q" для выхода.')

while True:
    input_data = input('Введите числа через пробел: ')

    if 'q' in input_data:  # Если есть специальный символ в полученной строке.
        # Выходим из цикла, если символ стоит только символ выхода.
        if len(input_data.split()) == 1:
            break

        # Если помимо спецсимвола есть другие символы.
        else:
            end = True  # Переменная end принимает значение True, чтобы после вывода выйти из цикла.
            # Оставляем только символы перед спецсимволом.
            for i in range(len(input_data)):
                if input_data[i] == 'q':
                    input_data = input_data[:i]
                    break

    lst = list(map(float, input_data.split()))
    s += sum(lst)
    print(f'Сумма чисел: {sum(lst)}. Итоговая сумма: {s}')
    if end:
        break
