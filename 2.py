with open('text_2.txt', 'r', encoding='utf-8') as file:
    word_count = 0
    for i, string in enumerate(file, 1):
        print(f'Количество слов в {i}-й строке: {len(string.split())}')
        word_count += len(string.split())

print(f'\nКоличество строк: {i}')
print(f'Всего слов: {word_count}')
