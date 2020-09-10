words = input('Введите несколько слов, разделенных пробелами: ').split()
print(f'Вы ввели {len(words)} слов(а/о).')
for i in range(len(words)):
    print(f'{i+1}-е слово: {words[i][:10]}')
