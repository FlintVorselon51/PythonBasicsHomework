class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина "{self.name}" начала движение.')

    def stop(self):
        print(f'Машина "{self.name}" остановилась.')

    def turn(self, direction):
        print(f'Машина "{self.name}" установила курс на "{direction}"')

    def show_speed(self):
        print(f'Машина "{self.name}" едет со скоростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Машина "{self.name}" превысила максимально допустимую скорость (60)!')
        Car.show_speed(self)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Машина "{self.name}" превысила максимально допустимую скорость (40)!')
        Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)  # Полицейская машина не может быть неполицейской


car_1 = Car(80, 'green', 'Reno Logan', False)
town_car_1 = TownCar(80, 'blue', 'Mazda CX5', False)
town_car_2 = TownCar(50, 'black', 'Lada Kalina', False)
work_car_1 = WorkCar(50, 'yellow', 'Toyota Camry', False)
work_car_2 = WorkCar(30, 'red', 'Жигули', False)
sport_car = SportCar(150, 'white', 'Tesla Roadster', False)
police_car = PoliceCar(90, 'pink', 'Приора')  # Не указываем, что это полицейская машина

car_1.show_speed()
town_car_1.show_speed()
town_car_2.show_speed()
work_car_1.show_speed()
work_car_2.show_speed()
sport_car.show_speed()
print(police_car.is_police)
