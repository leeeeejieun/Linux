import json

file = 'seoul.json'

with open(file) as f:
    data = json.load(f)

print(data)
data['population'] =' 30000000'
print(data)

with open(file, 'w') as f:
    new_data = [data]
    new_data.append({"city": 'Busan', 'population': 15024650})
    json.dump(new_data, f)
