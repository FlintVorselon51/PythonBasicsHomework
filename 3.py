class ItIsNotNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


lst = list()
while True:
    input_data = input('Введите строку: ')
    if input_data == 'stop':
        print(f'Получившийся в результате работы список: {lst}')
        break
    try:
        if not input_data.isdigit():
            raise ItIsNotNumberError(f'Введенная вами строка не является числом и не будет помещена в список.')
    except ItIsNotNumberError as error:
        print(error)
    else:
        print('Число успешно добавлено в список.')
        lst.append(int(input_data))
