
class MyString(str):
    def __add__(self, other):
        return str(self) + str(other)
    def __sub__(self, other):
        return self.replace(str(other), '', 1)


print('New' + MyString(890))
print(MyString(1234) + 5678)
print(MyString('New' + 'castle'))
print(MyString('New') + 77)
print(MyString('New') + True)
print(MyString('New') + ['s', ' ', 23])
print(MyString('New') + None)

print(MyString('New bala7nce') - 7)
print(MyString('New balance') - 'bal')
print(MyString('New balance') - 'Bal')
print(MyString('pineapple apple pine') - 'apple')
print(MyString('New balance') - 'apple')
print(MyString('NoneType') - None)
print(MyString(55678345672) - 7)
