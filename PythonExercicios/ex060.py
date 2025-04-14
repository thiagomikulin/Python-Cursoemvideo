print('CALCULADOR DE FATORIAL')
num = int(input('Digite um número qualquer: '))
cont = num
f = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))
