jumin = ''.join(input('주민등록번호를 입력하세요 > ').strip().split('-'))
# jumin = '821010-1635210'

check_num = [2,3,4,5,6,7,8,9,2,3,4,5]

jumin_num = [int(j) for j in jumin]

first_result = 0
for n,j in zip(jumin_num,check_num):
    first_result += n*j

second_result = 11 - (first_result % 11)
if second_result == jumin_num[-1]:
    print('유효하다.')
else:
    print('유효하지 않다.')
