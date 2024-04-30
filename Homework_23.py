import math
from task_03 import Point


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f'Circle(x={self.x}, y={self.y}, radius={self.radius})'

    def __add__(self, other):
        return Circle(self.x + other.x, self.y + other.y, self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __sub__(self, other):
        if self.radius - other.radius == 0:
            return Point(abs(self.x - other.x), abs(self.y - other.y))
        else:
            return Circle(abs(self.x - other.x), abs(self.y - other.y), abs(self.radius - other.radius))

x_1 = Circle(1, 2, 1)
x_2 = Circle(2, 5, 1)
x_3 = Circle(2, 2, 2)
x_4 = Circle(4, 3, 5)
print(x_1 - x_2)
print(x_3 - x_4)