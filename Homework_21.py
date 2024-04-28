# brand, age, cоlor, mark і weight
# move, birthday stop

class Auto:
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

auto_1 = Auto('Audi', 5, "A6")
print(auto_1.__dict__)
print(auto_1.birthday())
print(auto_1.brand)
print(auto_1.color)
print(auto_1.mark)
auto_1.move()
auto_1.stop()
auto_1.birthday()

