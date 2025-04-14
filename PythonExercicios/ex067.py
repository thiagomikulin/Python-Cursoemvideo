print(' - ' * 10)
print(' ' * 10, 'TABUADA', ' ' * 8)
print(' - ' * 10)
while True:
    n = int(input('Digite um número: '))
    cont = 0
    if n < 0:
        break
    while cont <= 10:
        print('{} X {} = {}'.format(n, cont, n * cont))
        cont += 1
