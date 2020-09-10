rating = [9.11, 8.0, 8.0, 6.66, 5.0, 1.01]

while True:
    print(f'Рейтинг: {rating}')
    number = float(input('Введите число: '))
    for i in range(len(rating)):
        if number > rating[i]:
            rating.insert(i, number)
            break
    else:
        rating.append(number)
