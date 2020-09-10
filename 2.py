lst = list()
n = int(input('Введите число элементов в списке: '))
for k in range(n):
    lst.append(input(f'Введите {k + 1}-й элемент массива: '))

print(f'Изначальный список: {lst}')

for i in range(1, n, 2):
    lst[i], lst[i-1] = lst[i-1], lst[i]

print(f'Список после перестановки: {lst}')
