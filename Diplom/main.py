import datetime
import json
import re
while True:
    class Human:

        def __init__(self, name, birthday, deathday=''):
            self.name = name
            self.birthday = str(birthday)
            self.deathday = str(deathday)

        def full_year(self):
            if self.deathday != '':
                self.birthday = re.split('[/. -]', self.birthday)
                self.deathday = re.split('[/. -]', self.deathday)
                birthday_year = int(self.birthday[2])
                birthday_month = int(self.birthday[1])
                birthday_day = int(self.birthday[0])
                deathday_year = int(self.deathday[2])
                deathday_month = int(self.deathday[1])
                deathday_day = int(self.deathday[0])
                years = deathday_year - birthday_year
                if birthday_month > deathday_month:
                    years -= 1
                elif birthday_month == deathday_month:
                    if birthday_day > deathday_day:
                        years -= 1
                # return years
            else:
                now = datetime.date.today()
                self.birthday = re.split('[/. -]', self.birthday)
                birthday_year = int(self.birthday[2])
                birthday_month = int(self.birthday[1])
                birthday_day = int(self.birthday[0])
                years = now.year - birthday_year
                if birthday_month > now.month:
                    years -= 1
                elif birthday_month == now.month:
                    if birthday_day > now.day:
                        years -= 1
            return years

        def data_read(self):
            with open('file_json.json') as file:
                data = json.load(file)
            return data

        def data_save(self):
            with open('file_json.json', 'w') as file_json:
                json.dump(data, file_json)
            return data

        def find_names(user):
            with open('file_json.json') as file:
                new_data = json.load(file)
                res = list()
                for k, v in new_data.items():
                    if str(user) in str(v):
                        res.append((k, v))
                return res
            print(res)
            # for i in res:
            #     print(i)

    poz = int(input('1 - завантаження бази даних, 2 - введення даних вручну, 3 - збереження даних, '
              '4 - пошук особи. Введіть необхідне число: '))

    if poz == 1:
        with open('file_json.json') as file:
            data = json.load(file)
        print(data)

    elif poz == 2:
        name = (input('Введіть ім\'я: ').title())
        surname = (input('Введіть прізвище: ').title())
        secondname = (input('Введіть пo батькові: ').title())
        birthday = str(input('Введіть дату народження у форматі д/м/рік: '))
        deathday = str(input('Введіть дату смерті (якшо є) у форматі д/м/рік: '))
        sex = str((input('Виберыть вашу стать (необовязково) у форматі: [M] - чол, [F] - жін, '': ')).upper())
        full = Human(name=name, birthday=birthday, deathday=deathday)
        data = {'name': name, 'surname': surname, 'secondname': secondname,
                'birthday': birthday, 'deathday': deathday, 'sex': sex, 'full year':  full.full_year()}
        print(data)
        Human.data_save(self=data)
    elif poz == 3:
        with open('file_json.json') as file:
            new_data = json.load(file)

    elif poz == 4:
        print(Human.find_names(user=input('Кого шукаєте?: ')))

    else:
        print('Введеного числа немає у списку варіантів. Спробуйте знову')

pass
