# TODO
# Реализовать класс Road (дорога);
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого
# для покрытия всей дороги;

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count(self):
        self.weight = self._length * self._width * 25 * 5
        return self.weight

a = Road(20, 5000)
b = Road(40, 5000)

print(a.count())
print(b.count())
