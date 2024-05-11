import json
data = {123123: ["Tom", 6], 456456: ["Bob", 11], 789789: ["Brenda", 8], 147147: ["Bill", 12], 258258: ["Glen", 9], 369369: ["Sam", 7]}

with open('file_json.json', 'w') as file_json:
    json.dump(data, file_json)