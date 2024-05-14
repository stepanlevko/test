import datetime
class Human:
    def year(self):
        self.birthday = str(birthday)
        now = datetime.date.today()
        birthday_year = int(self.birthday.split()[2])
        print(self.birthday[2])
        birthday_month = int(self.birthday.split()[1])
        birthday_day = int(self.birthday.split()[0])
        years = now.year - int(birthday_year)
        if birthday_month > now.month:
            years -= 1
        elif birthday_month == now.month:
            if birthday_day > now.day:
                years -= 1
        return years

birthday = Human('12 12 1212')
print(birthday.year())





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

