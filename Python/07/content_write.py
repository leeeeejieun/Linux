import os
content = """Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!"""

file = 'file.txt'

with open(file, 'w') as f:
    f.write(content)

with open(file, 'r') as f:
   lines = f.readlines()
   new_lines = [line.rstrip() for line in lines]
   print(new_lines)

if os.path.exists(file):
    answer = input('파일을 정말 삭제하시겠습니까? (y/n) :  ')
    if answer.lower().startswith('y'):
        os.remove(file)
