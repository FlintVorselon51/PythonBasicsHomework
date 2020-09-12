def describe_user(first_name, second_name, year_of_birth, city, email, phone):
    """Возвращает строку, в которой находится информация о пользователе."""
    string = 'Пользователя зовут ' + first_name + ' ' + second_name
    string += '.\nПользователь родился в ' + str(year_of_birth) + ' году, живёт в городе ' + city
    string += '.\nДля связи с пользователем имспользуйте email ' + email + ' или телефон ' + phone
    return string


print(describe_user(email='Ivanov@ivan.ru', phone='8-800-555-35-35', year_of_birth=988, city='Санкт-Петербург',
                    first_name='Иван', second_name='Иванов'))
