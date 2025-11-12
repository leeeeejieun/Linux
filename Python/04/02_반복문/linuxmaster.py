marks = [90, 25, 67, 45, 80]

# 인덱스 값을 받아오기
for index, mark in enumerate(marks):
    index += 1
    if mark >= 60:
        print(f'{index}번 학생: 합격')
    else:
        print(f'{index}번 학생: 불합격')