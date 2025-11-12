import requests

url = "https://jsonplaceholder.typicode.com/users"

data = {"name": "Bob", "email": "bab@example.com"}
rep = requests.put(url, json=data)
print(rep.headers)