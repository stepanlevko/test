data = {'name': 'Bob', 'age': 34, 'city': 'Dnipro', 'home': 'Bob'}

def find_names(user):
    res = []
    for k, v in data.items():
        if user in str(v):
            res.append((k, str(v)))
    return res

result = find_names(input('Введите имя: '))
print(result)
for i in result:
    print(i)



