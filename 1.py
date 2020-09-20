print('Введённые вами данные сохраняются в файл 1.txt.')
with open('1.txt', 'w', encoding='utf-8') as file:
    while True:
        data = input()
        if data != '':
            file.write(data+'\n')
        else:
            break
