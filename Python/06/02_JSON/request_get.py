import requests

url = "https://jsonplaceholder.typicode.com/users/1"
rep = requests.get(url)
print(rep.json())
print(rep.headers)
print(rep.text)