def func(a):
    res = 1
    for i in range(1, a + 1):
        res *= i
        yield res


n = int(input('Введите n: '))
[print(f'{j}! = {el}') for j, el in enumerate(func(n), 1)]

