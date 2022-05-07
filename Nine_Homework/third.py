# TODO
# Реализовать базовый класс Worker (работник)
# определить атрибуты: name, surname, position (должность),
# income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например:
# {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения
# полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage" : wage,
            "bonus" : bonus
            }

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print (f'Full name: {self.name} {self.surname}')

    def get_total_income(self):
        print ('Wage:', self._income["wage"] + self._income["bonus"])


michail = Position('Michail', 'Zadornov', 'Jocker', 20000, 5000)
michail.get_full_name()
michail.get_total_income()
