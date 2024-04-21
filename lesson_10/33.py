def num():
    if int(value) > 0:
        print('Ви ввели позитивне ціле число: ', value)
    elif int(value) < 0:
        print('Ви ввели негативне ціле число: ', value)
    else:
        print('Ви ввели мабуть ZERO: ', value)

while True:
    value = input('Введіть число: ')

    if value.isdigit():
        num

        if float(value.replace(',', '.', 1)) > 0:
            print('Ви ввели позитивне дробове число: ', value)
        elif float(value.replace(',', '.', 1)) < 0:
            print('Ви ввели негативне дробове число: ', value)
    elif value.upper() in ('EXIT', 'QUIT', 'ВИХІД', 'E', 'Q'):
        break
    elif value.isalpha():
        print('Ви ввели неоректне число: ', value)
    elif value.isalnum():
        print('Ви ввели неправильне число: ', value)

