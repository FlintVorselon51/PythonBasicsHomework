class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


pos = Position('Иван', 'Иванов', 'Программер', {'wage': 30000, 'bonus': 4000})
print(f'Должность сотрудника - {pos.position}')
print(f'Имя сотрудника - {pos.get_full_name()}')
print(f'Доход с учётом премии - {pos.get_total_income()}')
