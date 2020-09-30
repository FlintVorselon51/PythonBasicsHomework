from time import strptime


class Date:
    def __init__(self, string):
        self.string = string

    @classmethod
    def get_data(cls, self):
        return tuple(map(int, self.string.split('-')))

    @staticmethod
    def validation(self):
        try:
            valid_date = strptime(self.string, '%d-%m-%Y')
        except ValueError:
            return 'Строка не прошла валидацию!'
        else:
            return 'Строка успешно прошла валидацию!'


date_string_1 = '01-01-2020'
date_string_2 = '40-01-2020'

date_1 = Date(date_string_1)
date_2 = Date(date_string_2)

print(f'Извлекаем число (date_1): {Date.get_data(date_1)}')
print(f'Извлекаем число (date_2): {Date.get_data(date_2)}')
print(f'Проверяем дату (date_1): {Date.validation(date_1)}')
print(f'Проверяем дату (date_2): {Date.validation(date_2)}')
