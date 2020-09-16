proceeds = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))

if proceeds > costs:
    profit = proceeds - costs
    profitability = profit / proceeds
    print('Фирма работает в прибыль')
    print(f'Прибыль фирмы: {profit:.2f}')
    print(f'Рентабельность выручки: {profitability:.4f}')
    number_of_employees = int(input('Введите число сотрудников: '))
    profit_per_employee = profit / number_of_employees
    print(f'Прибыль на одного сотрудника: {profit_per_employee:.2f}')
elif proceeds < costs:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в ноль')
