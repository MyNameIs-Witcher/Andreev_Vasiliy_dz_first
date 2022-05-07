# TODO
# Создать класс TrafficLight (светофор)
# определить у него один атрибут color (цвет) и метод running (запуск)
# атрибут реализовать как приватный
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на мое усмотрение
from time import sleep

class TrafficLight:
    def __init__(self):
        self.__colour = {
            'red' : 7,
            'yellow' : 2,
            'green' : None
            }

    def running(self, colour, green_time):
        self.__colour['green'] = int(green_time)
        flag = False
        for key in self.__colour:
            if flag == False:
                if key != colour:
                    next
                else:
                    flag = True
                    print (key)
                    for i in range(self.__colour[key], 0, -1):
                        print (i, '...')
                        sleep(1)
            else:
                print (key)
                #sleep(self.__colour[key])
                for i in range(self.__colour[key], 0, -1):
                    print (i, '...')
                    sleep(1)


a = TrafficLight()
a.running('green', 10)

