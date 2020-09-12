def my_func(a, b, c):
    """Возвращает сумму двух максимальных переданных чисел."""
    return max(a + b, a + c, b + c)


print(my_func(17, 18, 5))
