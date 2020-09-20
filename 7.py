from json import dump
with open('text_7.txt', 'r', encoding='utf-8') as read_file:
    dictionary = {string.split()[0]: int(string.split()[2]) - int(string.split()[3]) for string in read_file}

average_profit_lst = []
for n in dictionary.values():
    if n > 0:
        average_profit_lst.append(n)
average_profit = sum(average_profit_lst) / len(average_profit_lst)
with open('text_77.json', 'w', encoding='utf-8') as write_file:
    dump([dictionary, {"average_profit": average_profit}], write_file, ensure_ascii=False, indent=4)
