import json
import csv
import random

with open('file_json.json') as file:
    input_data = json.load(file)

# phone = [098, 097, 096, 093, 067]
#
# for item in phone:
#     random item

keys = ['ID', 'Ім\'я', 'Вік', 'Телефон']
data_rows = []
for item in input_data:
    data = [item, input_data.get(item)[0], input_data.get(item)[1], ' ']
    for key in keys:
        data.append()
    data_rows.append(data)
print(data)
print(data_rows)

with open('task_02.csv', 'w', newline='') as file:
     file_writer = csv.writer(file, delimiter=',')
     file_writer.writerow(key)
     file_writer.writerows(data_rows)
