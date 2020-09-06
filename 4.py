number = int(input('Введите целое положительное число: '))
digit = 0
the_biggest_digit = 0

while number > 0:
    digit = number % 10
    if digit > the_biggest_digit:
        the_biggest_digit = digit
    number //= 10

print(f'Самая большая цифра в числе - {the_biggest_digit}')
