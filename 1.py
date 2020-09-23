from time import sleep


class TrafficLight:
    def __init__(self):
        self.__modes = ('red', 'yellow', 'green', 'yellow')
        self.__mode_counter = 0
        self.__durations = (7, 2, 5, 2)
        self.__color = self.__modes[0]

    def running(self):
        print(f'Сейчас светофор из состояния {self.__color}', end=' ')
        self.__mode_counter = self.__mode_counter + 1 if self.__mode_counter != len(self.__modes) - 1 else 0
        self.__color = self.__modes[self.__mode_counter]
        print(f'перешёл в состояние {self.__color}. '
              f'Через {self.__durations[self.__mode_counter]} секунд(ы) это состояние изменится.')
        sleep(self.__durations[self.__mode_counter])


traffic_light = TrafficLight()
print('Внимание! Бесконечный цикл!')
while True:
    traffic_light.running()
