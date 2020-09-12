def int_func(w):
    """
    Принимает строку. Возвращает строку с прописной первой буквой,
    если переданная строка состоит только из латинских букв в нижнем регистре.
    Иначе - возвращает переданную строку.
    """
    result = ''
    for i, sym in enumerate(w, 0):
        if not 97 <= ord(sym) <= 122:
            return w
        result += chr(ord(sym) - 32 if i == 0 else ord(sym))
    return result


string = input('Введите строку: ')
for word in string.split():
    print(int_func(word), end=' ')
