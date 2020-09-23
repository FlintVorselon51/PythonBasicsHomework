class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self):
        return self._length * self._width * 25 * 5 / 1000


road = Road(20, 5000)
print(f'{road.calculate_mass()} тонн')
