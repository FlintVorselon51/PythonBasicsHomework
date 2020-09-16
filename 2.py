number_of_seconds = int(input('Введите количество секунд: '))
number_of_minutes = number_of_seconds // 60
number_of_hours = number_of_minutes // 60

print(f'{number_of_hours:02}:{number_of_minutes % 60:02}:{number_of_seconds % 60:02}')
