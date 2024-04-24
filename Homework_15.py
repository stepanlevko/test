while True:
    value = input('Введіть число: ')

    if value.isdigit():
        print('Ви ввели позитивне ціле число: ', value)
    elif value.startswith('-') and value[1:].isdigit():
        print('Ви ввели негативне ціле число: ', value)
    elif (value.find('.') or value.startswith('.')) and value.replace(',', '.', 1) and not value.isalnum() and not value.startswith('-'):
        print('Ви ввели позитивне дробове число: ', value)
    elif value.startswith('-') and value.find('.') and value.replace(',', '.', 1):
        print('Ви ввели негативне дробове число: ', value)
    elif value.upper() in ('EXIT', 'QUIT', 'ВИХІД', 'E', 'Q'):
        break
    elif value.isalpha():
        print('Ви ввели неоректне число: ', value)
    elif value.isalnum():
        print('Ви ввели неправильне число: ', value)



