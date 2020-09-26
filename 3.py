class Cell:
    def __init__(self, cells):
        self.__cells = cells

    def make_order(self, n):
        s = ''
        c = self.__cells // n
        for i in range(c):
            s += '*' * n + '\n'
        s += '*' * (self.__cells % n)
        return s

    def __str__(self):
        return str(self.__cells)

    def __add__(self, other):
        if type(other) is Cell:
            return Cell(self.__cells + other.__cells)
        else:
            raise ValueError

    def __sub__(self, other):
        if type(other) is Cell:
            if self.__cells - other.__cells > 0:
                return Cell(self.__cells - other.__cells)
            else:
                return f'Разность двух ячеек - неположительное число. Если клетки поменять местами, то результат - ' \
                       f'{other.__cells - self.__cells}'
        else:
            raise ValueError

    def __mul__(self, other):
        if type(other) is Cell:
            return Cell(self.__cells * other.__cells)
        else:
            raise ValueError

    def __floordiv__(self, other):
        if type(other) is Cell:
            if (self.__cells / other.__cells).is_integer():
                return Cell(self.__cells // other.__cells)
            elif (other.__cells / self.__cells).is_integer():
                return f'При делении ячеек получается нецелое число - {self.__cells / other.__cells}' + \
                       f', но при замене получается целое - {other.__cells // self.__cells}'
            else:
                return f'При делении ячеек получается нецелое число - {self.__cells / other.__cells}'
        else:
            raise ValueError


cell_1 = Cell(10)
cell_2 = Cell(20)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_2 // cell_1)
print(cell_1 // cell_2)
print(Cell(11) // cell_1)

print()
print(cell_1.make_order(3))
print()
print(cell_2.make_order(7))
