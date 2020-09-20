list_of_special_employees = []
salary_sum = 0

with open('text_3.txt', 'r', encoding='utf-8') as file:
    for i, string in enumerate(file, 1):
        salary = float(string.split()[1])
        salary_sum += salary
        if salary < 20000:
            list_of_special_employees.append(string.split()[0])

print(f'Список сотрудников, оклад которых меньше 20000: {list_of_special_employees}')
print(f'Средняя величина дохода сотрудников - {salary_sum / i}')
