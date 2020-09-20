# Результат сохраняется в text_4_result.txt.
def translate_numeral(numeral):
    dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}  # ...?
    return dictionary[numeral]


result_data = ''
# Чтение.
with open('text_4.txt', 'r', encoding='utf-8') as read_file:
    for string in read_file:
        n = string.split()[0]
        result_data += translate_numeral(n) + string[len(n):]

# Запись.
with open('text_4_result.txt', 'w', encoding='utf-8') as write_file:
    write_file.write(result_data)
