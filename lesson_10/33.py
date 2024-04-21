# def number():
#     if int(value) > 0:
#         print('Ви ввели позитивне ціле число: ', value)
#     elif value.isdigit() < 0:
#         print('Ви ввели негативне ціле число: ', value)
#     elif float(value) > 0:
#         print('Ви ввели позитивне дробове число: ', value)
#     elif float(value) < 0:
#         print('Ви ввели негативне дробове число: ', value)

while True:
    value = input('Введіть число: ')

    if value != 0:
        if value.isdigit() > 0:
            print('Ви ввели позитивне ціле число: ', value)
        elif value.isdigit() < 0:
            print('Ви ввели негативне ціле число: ', value)
        elif float(value) > 0:
            print('Ви ввели позитивне дробове число: ', value)
        elif float(value) < 0:
            print('Ви ввели негативне дробове число: ', value)
    elif value.upper() in ('EXIT', 'QUIT', 'ВИХІД', 'E', 'Q'):
        break
    elif value.isalpha():
        print('Ви ввели неоректне число: ', value)
    elif value.isalnum():
        print('Ви ввели неправильне число: ', value)

