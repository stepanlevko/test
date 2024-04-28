import time
class Auto(object):
    pass
    def __init__(self, brand, age,  mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')
    def birthday(self):
        for item in range(self.age + 1):
            item += 1
        print(f'year birhday {item}')

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load
    def move(self):
        print('atention')
        super().move()
    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)
class Car(Auto):
    def __init__(self, brand, age, mark, max_speed):
        self.max_speed = max_speed
    def move(self):
        super().move()
        print('max speed is:', self.max_speed)


truck_1 = Truck('Volvo', 10, 'CX750', 15)
truck_2 = Truck('Reno', 8,  'T1500', 18)
car_1 = Car('Audi', 5, 'A6', 250)
car_2 = Car('ZEEKR', 1, '001', 220)
print(truck_1.__dict__)
truck_1.move()
truck_1.load()
print(truck_2.__dict__)
truck_2.move()
truck_2.load()
print(car_1.__dict__)
car_1.move()
print(car_2.__dict__)
car_2.move()
