from random import randint

# Генерируем от 5 до 10 случайных целых чисел от -100 до 100.
numbers = [randint(-100, 100) for _ in range(randint(5, 10))]

# Записываем получившиеся числа в файл.
with open('text_5.txt', 'w', encoding='utf-8') as write_file:
    [write_file.write(str(n) + ' ') for n in numbers]

# Можно уже сейчас посчитать сумму чисел, но, как я понял, нужно прочитать числа из файла.
with open('text_5.txt', 'r', encoding='utf-8') as read_file:
    print(f'Сумма чисел равна {sum(list(map(int, read_file.read().split())))}')
