address = input('address: ')
# address = 'http://www.naver.com/edit/page/7022'

domain = address.split('/')[2].split('.')[-1]
print(f'domain: {domain}')