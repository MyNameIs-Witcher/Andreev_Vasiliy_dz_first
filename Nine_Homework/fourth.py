# TODO
# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты:
# speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, color, name, speed, is_police):
        self.color = color
        self.name = name
        self.speed = speed
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Car is going at speed {self.speed}')
    def stop(self):
        self.speed = 0
        print('Car stopped')
    def turn(self, direction):
        self.direction = direction
        print(f'Car turn {self.direction}')
    def show_speed(self):
        print(f'Car speed: {self.speed}')

class TownCar(Car):
    def __init__(self, color, name, speed = 0, is_police = False):
        super().__init__(color, name, speed, is_police)
    def show_speed(self):
        if self.speed > 60:
            print(f'Car speed: {self.speed} it is too high!')
        else:
            print(f'Car speed: {self.speed}')

class SportCar(Car):
    def __init__(self, color, name, speed = 0, is_police = False):
        super().__init__(color, name, speed, is_police)

class WorkCar(Car):
    def __init__(self, color, name, speed = 0, is_police = False):
        super().__init__(color, name, speed, is_police)
    def show_speed(self):
        if self.speed > 40:
            print(f'Car speed: {self.speed} it is too high!')
        else:
            print(f'Car speed: {self.speed}')

class PoliceCar(Car):
    def __init__(self, color, name, speed = 0, is_police = True):
        super().__init__(color, name, speed, is_police)
print('Car a')
a = TownCar('red', 'bugatti')
print (f'It is police car? {a.is_police}')
a.show_speed()
a.go(45)
a.show_speed()
a.stop()
a.go(80)
a.turn('left')
a.show_speed()
a.stop()

print('Car b')
b = PoliceCar('blue', 'VAZ-2105')
print (f'It is police car? {b.is_police}')
b.show_speed()
b.go(20)
b.show_speed()
b.stop()
b.go(80)
b.turn('right')
b.show_speed()
b.stop()
