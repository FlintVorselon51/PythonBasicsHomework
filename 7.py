class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        z = '+' if self.b > 0 else '-'
        if self.b == 0:
            return f'{self.a}'
        return f'{self.a} {z} {abs(self.b)}*i'


complex_1 = ComplexNumber(2, 1)
complex_2 = ComplexNumber(9, -7)
complex_3 = ComplexNumber(-5, 0)

print(complex_1)
print(complex_2)
print(complex_3)

print()

print(complex_1 + complex_2)
print(complex_1 + complex_3)
print(complex_2 + complex_3)

print()

print(complex_1 * complex_2)
print(complex_1 * complex_3)
print(complex_2 * complex_3)
