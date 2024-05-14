import datetime

birthday = '14 05 2000'

# print(birthday)
now = datetime.date.today()
# print(birthday.split()[2])
birthday_year = int(birthday.split()[2])
# print(birthday_year)
birthday_month = int(birthday.split()[1])
# print(birthday_month)
birthday_day = int(birthday.split()[0])
years = now.year - birthday_year

if birthday_month > now.month:
    years -= 1
elif birthday_month == now.month:
    if int(birthday_day) > now.day:
        years -= 1
print(years)




