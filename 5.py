class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'"{self.title}" сообщает: "запуск отрисовки"')


class Pen(Stationery):
    def draw(self):
        print(f'Ручка "{self.title}" сообщает: "запуск отрисовки"')


class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш "{self.title}" сообщает: "запуск отрисовки"')


class Handle(Stationery):
    def draw(self):
        print(f'Маркер "{self.title}" сообщает: "запуск отрисовки"')


stationery = Stationery('Принадлежность')
pen = Pen('Супер-ручка')
pencil = Pencil('Мистер карандаш')
handle = Handle('Меня не ототрёшь')

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
