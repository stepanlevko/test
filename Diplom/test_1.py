import json
name = (input('Введіть ім\'я: '))
surname = (input('Введіть прізвище: '))
secondname = (input('Введіть пo батькові: '))
birthday = str((input('Введіть дату народження у форматі д м рік: ')))
deathday = str((input('Введіть дату смерті (якшо є) у форматі д м рік: ')))
        # Human.save_data =
        # Human.data_input
data = {'name': name, 'surname': surname, 'secondname': secondname,
                'birthday': birthday, 'deathday': deathday}
with open('file_json.json', 'w') as file_json:
    json.dump(data, file_json)
# return data_load

print(data)
# print(data_load)
