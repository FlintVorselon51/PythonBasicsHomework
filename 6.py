from itertools import count, cycle

# а)
iterator = count(int(input('Введите целое число, начиная с которого будут генерироваться числа: ')))
print('Первые десять чисел начиная с введенного вами числа:')
for i in range(10):
    print(next(iterator), end=' ')

# б)
print('\n- cycle -')
lst = ['string', 101, 3.1415, 15.457]
iterator = cycle(lst)
# Перебираем элементы списка два раза.
for i in range(len(lst) * 2):
    print(next(iterator), end=' ')
