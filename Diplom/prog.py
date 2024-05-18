# from main import Human
import datetime
import re
class Human:
    def __init__(self, birthday, deathday=''):
        self.birthday = str(birthday)
        self.deathday = str(deathday)
        # self.full_year()


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
            return years
        elif self.deathday == '':
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

birthday = '16/05/2014'
deathday = Human('16/05/2014', deathday='16/05/2016')
print(deathday)
full = Human.full_year
# Human.full_year
print(Human.full_year)
# print(Human.full_year(self=''))

