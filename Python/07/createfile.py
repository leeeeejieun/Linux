import os

path = '/home/soldesk/test'
file = os.path.join(path, 'test.txt')
content = '''
반갑습니다. 
python 개발자 여러분 한살 더 드셨죠!
올 한해는... 행복한 가득한 한해가 되었으면 합니다.
'''

if not os.path.isdir(path):
    os.mkdir(path)

with open(file, 'w') as f:
    f.write(content)

with open(file, 'r') as f:
    print(f.read())

if os.path.isfile(file):
    answer = input('파일을 정말 삭제하시겠습니까? (y/n) :  ')
    if answer.lower().startswith('y'):
        os.remove(file)

