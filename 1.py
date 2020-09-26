class Matrix:

    def __init__(self, lst):
        self.__size = (len(lst), max([len(i) for i in lst]))
        self.__max_el_len = 0
        for i in lst:
            for j in i:
                if len(str(j)) > self.__max_el_len:
                    self.__max_el_len = len(str(j))
        for i in lst:
            for _ in range(self.__size[1] - len(i)):
                i.append(0)
        self.__lst = lst

    def __add__(self, other):

        lst = []

        if type(other) is int:
            for i in range(len(self.__lst)):
                lst.append([j + other for j in self.__lst[i]])

        elif type(other) is Matrix:
            other_lst = other.get_lst()
            if self.__size != other.get_size():
                print('Невозможно сложить эти две матрицы!')
                raise ValueError
            else:
                for i in range(self.__size[0]):
                    line = []
                    for j in range(self.__size[1]):
                        line.append(self.__lst[i][j] + other_lst[i][j])
                    lst.append(line)

        return Matrix(lst)

    def __str__(self):
        s = ''
        for i in self.__lst:
            for j in i:
                s += str(j) + (' ' * (self.__max_el_len - len(str(j)) + 3))
            s += '\n'
        return s

    def get_size(self):
        return self.__size

    def get_lst(self):
        return self.__lst


matrix_1 = Matrix([[1, 20, 3], [4, 5, 6]])
matrix_2 = Matrix([[10, 20, 30], [40, 50, 60]])
sum_1 = matrix_1 + 10  # Матрицу можно сложить не только с матрицей, но и с числом.
sum_2 = matrix_1 + matrix_2  # Складываем две матрицы

print('Матрица из "неровного" списка:')
print(Matrix([[1, 2, 3], [4], [5, 6]]))  # Если передать "неровный" список, то недостающие значение заполнятся нулями.

print('\nМатрица #1:', matrix_1, '\nМатрица #2:', matrix_2, '\nМатрица #1 + 10:', sum_1,
      '\nМатрица #1 + Матрица #2:', sum_2, sep='\n')
