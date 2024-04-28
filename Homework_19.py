import json
import csv

with open('task_01.json') as file:
    input_data = json.load(file)

input_data = list(input_data.items())


data_rows = []
for item in input_data:
    data = []
    keys = ['ID', 'Ім\'я', 'Вік', 'Телефон']
    for key in keys:
        data.append(item)
    data_rows.append(data)

print(data_rows)

with open('task_02.csv', 'w', encoding='utf-8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',')
    file_writer.writerow(keys)
    file_writer.writerows(item)
