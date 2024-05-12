def func(self, other, a):
    while a < 6:
        yield self * (other ** a)
        a += 1

for item in func(-2, -5, 0):
    print(item)

for item in func(10, 3, 0):
    print(item)