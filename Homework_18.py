import json

input_data = {'123123': ('Tom', 6), '456456': ('Bob', 11), '789789': ('Brenda', 8), '147147': ('Bill', 12), '258258': ('Glen', 9), '369369': ('Sam', 7)}

with open('task_01.json', 'w') as file:
    json.dump(input_data, file)

with open('task_01.json') as file:
    data_2 = json.load(file)

print(input_data)
print(data_2)
