# paths = input('Path: ')

paths = '/etc/security/pam_security.so'

path = '/'.join(paths.split('/')[:-1])
file = paths.split('/')[-1]

print(f'path: {path}')
print(f'file: {file}')