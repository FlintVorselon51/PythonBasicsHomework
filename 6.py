products = list()
empty_parameter_dictionary = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
analytics = {parameter: [] for parameter in empty_parameter_dictionary.keys()}

while True:
    command = input('Введите команду (Введите "help", чтобы получить список доступных команд): ')

    if command == 'help':
        print('Доступные команды:')
        print('Введите "0" или "q", если хотите выйти')
        print('Введите "1" или "add", для того, чтобы добавить товар')
        print('Введите "2" или "get", для того, чтобы получить аналитку')

    elif command in ('0', 'q'):
        break

    elif command in ('1', 'add'):
        parameter_dictionary = empty_parameter_dictionary
        for p in empty_parameter_dictionary.keys():
            input_data = input(f'Введите значение параметра "{p}": ')
            parameter_dictionary[p] = int(input_data) if input_data.isdigit() else input_data
        products.append((len(products) + 1, parameter_dictionary.copy()))

    elif command in ('2', 'get'):
        if len(products) == 0:
            print('Вы не добавили ни одного товара. Используйте команду "1", для того, чтобы добавить первый товар')
        else:
            analytics = {parameter: [] for parameter in empty_parameter_dictionary.keys()}
            for product in products:
                for k in product[1].keys():
                    if not product[1][k] in analytics[k]:
                        analytics[k].append(product[1][k])
            print('Аналитика:')
            for k, v in analytics.items():
                print(f'"{k}:" {v}')
