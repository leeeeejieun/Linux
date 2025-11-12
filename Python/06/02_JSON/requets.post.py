import requests

url = "https://jsonplaceholder.typicode.com/users"

data = {"name": "Bob"}
rep = requests.post(url, json=data)
print(rep.json())