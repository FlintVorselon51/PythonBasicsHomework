result_now = float(input('Введите результат спортсмена в первый день: '))
goal = float(input('Введите желаемый результат: '))
day = 1
while result_now < goal:
    day += 1
    result_now *= 1.10

print(f'На {day}-й день спортсмен достиг желаемого результата')
