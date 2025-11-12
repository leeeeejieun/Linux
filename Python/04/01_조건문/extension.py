filenames = ['intra.h', 'intra.c', 'input.txt', 'run.py']

result = [f for f in filenames if f.endswith('.h') == True or f.endswith('.c') == True]
print(result)