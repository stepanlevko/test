import datetime
import json
import csv
import re
while True:
    class Human:

        def __init__(self, name, birthday, deathday=''):
            self.name = name
            self.birthday = str(birthday)
            self.deathday = str(deathday)

        def full_year(self):
            self.birthday = re.split('[/. -]', self.birthday)
            birthday_year, birthday_month, birthday_day = int(self.birthday[2]), int(self.birthday[1]), int(
                self.birthday[0])
            if self.deathday != '':
                self.deathday = re.split('[/. -]', self.deathday)
                year, month, day = int(self.deathday[2]), int(self.deathday[1]), int(self.deathday[0])
            elif self.deathday == '':
                now = datetime.date.today()
                year, month, day = now.year, now.month, now.day
            years = year - birthday_year
            if birthday_month > month:
                years -= 1
            elif birthday_month == month:
                if birthday_day > day:
                    years -= 1
            return years

        def data_read(self):
            with open('file_json.json') as file:
                data = json.load(file)
            return data

        def data_save(self):
             with open('file_json.json', 'a', newline='\n', encoding='utf-8') as file_json:
                 json.dump(data, file_json, indent=1, ensure_ascii=False)
             return data

        def find_names(user):
            with open('file_json.json', encoding='utf-8') as file:
                new_data = json.load(file)
                res = []
                for k, v in new_data.items():
                    if str(user) in str(v):
                        res.append((k, v))
                return res
            print(res)
    try:
        poz = int(input('1 - завантаження бази даних, 2 - введення даних вручну, '
                        '3 - пошук особи. Введіть необхідне число: '))

        if poz == 1:
            with open('file_json.json', encoding='utf-8') as file:
                data = json.load(file)
            print(data)
        elif poz == 2:
            try:
                name = (input('Введіть ім\'я: ').title())
                surname = (input('Введіть прізвище: ').title())
                secondname = (input('Введіть пo батькові: ').title())
                birthday = str(input('Введіть дату народження у форматі д/м/рік: '))
                deathday = str(input('Введіть дату смерті (якшо є) у форматі д/м/рік: '))
                sex = str((input('Виберіть вашу стать (необов\'язково) у форматі: [M] - чол, [F] - жін, '': ')).upper())
                full = Human(name=name, birthday=birthday, deathday=deathday)
                data = {
                    'name': name,
                    'surname': surname,
                    'secondname': secondname,
                    'birthday': birthday,
                    'deathday': deathday,
                    'sex': sex,
                    'full year':  full.full_year()
                }
                print(data)
                Human.data_save(data)
            except IndexError:
                print('Введіть коректне значення')
        elif poz == 3:
            print(Human.find_names(user=input('Кого шукаєте?: ').title()))
        elif poz != 1 and 2 and 3 and poz is not int():
            print('Введеного числа немає у списку варіантів. Спробуйте знову')
    except ValueError:
        print('Введіть коректне значення')
pass
