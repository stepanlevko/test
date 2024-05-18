import datetime
import re
class Human:

    def __init__(self, birthday, deathday=''):
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

birthday = str(input('date: ', ))
deathday = str(input('date: ', ))

full = Human(birthday=birthday, deathday=deathday)
print(full.full_year())



# birthday = input('date: ')
# deathday = input('date: ')

# if deathday != None:
#     print(Human.year())
# else:
#     print(Human.year())








#
# poz = int(input('1 - завантаження бази даних, 2 - введення даних вручну, 3 - збереження даних, '
#           '4 - пошук особи. Введіть необхідне число: '))
#
# # if poz == 1:
# #     Human.data_load
# if poz == 2:
#     # name = (input('Введіть ім\'я: '))
#     # surname = (input('Введіть прізвище: '))
#     # secondname = (input('Введіть пo батькові: '))
#     birthday = str((input('Введіть дату народження у форматі д м рік: ')))
#     deathday = str((input('Введіть дату смерті (якшо є) у форматі д м рік: ')))
#
# elif poz == 3:
#     pass
# elif poz == 4:
#     pass
# else:
#     print('Введеного числа немає у списку варіантів. Спробуйте знову')

