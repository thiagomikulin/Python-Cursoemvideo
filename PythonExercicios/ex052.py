num = int(input('Digite um número:'))
tot = 0

for n in range(1, num+1):
    if num % n == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(n, end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Esse é um número primo')
else:
    print('Esse não é um número primo')
