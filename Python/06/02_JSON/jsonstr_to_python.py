import json

json_data = '{"name": "Alice", "age": 25, "hobby": ["reading", "music"]}'

python_obj = json.loads(json_data)
python_obj['age'] = 25
print(python_obj['age'])


print(json.dumps(python_obj))
