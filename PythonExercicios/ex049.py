num = int(input('Digite um número'))
print('-'*20)
for n in range(1, 11, 1):
    print('{} X {:2} = {}'.format(num, n, num * n))
