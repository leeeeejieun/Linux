import requests

url = "https://jsonplaceholder.typicode.com/users/1"

rep = requests.delete(url)
print(rep.headers)
print(rep.text)