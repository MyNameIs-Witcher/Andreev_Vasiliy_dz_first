# TODO
# Реализовать класс Stationery
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
#создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;

class Stationery:
    def __init__(self, title = None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки!')
        if self.title:
            print(f'Выбран инструмент {self.title}')

class Pen(Stationery):
    def __init__(self, title = 'Ручка'):
        super().__init__(title)
    def draw(self):
        print(f'Запуск отрисовкиб используется {self.title}')

class Pencil(Stationery):
    def __init__(self, title = 'Карандаш'):
        super().__init__(title)
    def draw(self):
        print(f'Запуск отрисовки используется {self.title}')

class Handle(Stationery):
    def __init__(self, title = 'Маркер'):
        super().__init__(title)
    def draw(self):
        print(f'Запуск отрисовки используется {self.title}')

a = Pencil()
a.draw()

b = Handle()
b.draw()

c = Stationery()
c.draw()
