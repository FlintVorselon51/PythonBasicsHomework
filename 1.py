lst = [1234, 13.37, complex(12, 13), True, 'some text', (1, 4, 8, 8), [2, 0, 4, 8],
       {'answer': 42, 'error_key': 404, 'value': 666}, {3.1415, 2.7182, 1.6180}, frozenset((0, 1, 5, 8)), None,
       bytes([8, 88, 188])]

for el in lst:
    print(f'Объект {el} имеет тип {type(el).__name__}')
