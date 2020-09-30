class ItIsNotNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    def __init__(self):
        self.office_equipment = []  # Оргтехника, находящаяся на складе.
        self.in_departments = {}  # Оргтехника, находящаяся в подразделениях.

    def take_to_storage(self, *equipment):  # Метод, отвечающий за принятие на склад оргтехники.
        for eq in equipment:
            self.office_equipment.append(eq)

    def write_off(self, *equipment):  # Метод, отвечающий за списывание оргтехники со склада.
        for eq in equipment:
            if eq in self.office_equipment:
                self.office_equipment.remove(eq)

    def send_to_department(self, department, *equipment):  # Метод, отвечающий за отправку оргтехники в подразделения.
        for eq in equipment:
            if eq in self.office_equipment:
                self.office_equipment.remove(eq)
                if department in self.in_departments.keys():
                    self.in_departments[department].append(eq)
                else:
                    self.in_departments[department] = [eq]
            else:
                print(f'Объекта\n???\n{eq}???\nнет на складе!')

    def take_from_department(self, department, *equipment):  # Метод, отвечающий за возвращение оргтехники из отдела.
        for eq in equipment:
            if eq in self.in_departments[department]:
                self.in_departments[department].remove(eq)
                self.office_equipment.append(eq)

    def __str__(self):
        s = '~~~~~ Состояние склада ~~~~~\n'
        if not self.office_equipment:
            return s + 'Сейчас на складе пусто.\n'
        for eq in self.office_equipment:
            s += str(eq)
        return s + '\n'


class OfficeEquipment:
    def __init__(self, amount, cost):  # Принимает количество оргтехники и стоимость.
        self.cost = cost
        try:
            if not str(amount).isdigit():
                self.amount = 0
                raise ItIsNotNumberError('Количество оргтехники должно быть числом!')
        except ItIsNotNumberError as error:
            print(error)
        else:
            self.amount = int(amount)

    def __str__(self):
        return f'--- Партия оргтехники ---\n' \
               f'Количество: {self.amount}; Стоимость: {self.cost}\n'


class Printer(OfficeEquipment):
    def __init__(self, amount, cost, capacity, print_speed):  # Уникальные параметры: ёмкость и скорость печати.
        super().__init__(amount, cost)
        self.capacity = capacity
        self.print_speed = print_speed

    def __str__(self):
        return f'--- Партия принтеров ---\n' \
               f'Количество: {self.amount}; Стоимость: {self.cost}; ' \
               f'Ёмкость: {self.capacity}; Скорость печати: {self.print_speed}\n'


class Scanner(OfficeEquipment):
    def __init__(self, amount, cost, resolution, color_depth):  # Уникальные параметры: разрешение и глубина цвета.
        super().__init__(amount, cost)
        self.resolution = resolution
        self.color_depth = color_depth

    def __str__(self):
        return f'--- Партия сканеров ---\n' \
               f'Количество: {self.amount}; Стоимость: {self.cost}; ' \
               f'Разрешение: {self.resolution}; Глубина цвета: {self.color_depth}\n'


class Xerox(OfficeEquipment):
    # Уникальные параметры: формат сканирования и количество катриджей.
    def __init__(self, amount, cost, scan_format, number_of_cartridges):
        super().__init__(amount, cost)
        self.scan_format = scan_format
        self.number_of_cartridges = number_of_cartridges

    def __str__(self):
        return f'--- Партия ксероксов ---\n' \
               f'Количество: {self.amount}; Стоимость: {self.cost}; ' \
               f'Формат сканирования: {self.scan_format}; Количество катриджей: {self.number_of_cartridges}\n'


storage = Storage()
set_of_printers = Printer(10, '60000р', '500л', '8л/м')
set_of_scanners = Scanner(15, '45000р', '1920x1080', '24бит')
set_of_photocopiers = Xerox(30, '75000р', 'А4', 20)

print(storage)

storage.take_to_storage(set_of_printers)  # Добавляем на склад принтеры.
print(storage)
storage.take_to_storage(set_of_scanners)  # Сканеры.
print(storage)
storage.take_to_storage(set_of_photocopiers)  # Ксероксы.
print(storage)

storage.write_off(set_of_printers)  # Списываем со склада принтеры.
print(storage)

storage.send_to_department('Отдел-1', set_of_scanners)  # Отправляем в подразделение сканеры
storage.send_to_department('Отдел-1', set_of_scanners)  # При попытке сделать это ещё раз, получаем сообщение об ошибке.
print(storage)

storage.take_from_department('Отдел-1', set_of_scanners)  # Возвращаем сканеры
print(storage)

# Указанное количество не является числом - вызываем исключение
set_of_scanners_ = Scanner('5а', '4000р', '1024x768', '12бит')
