n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))
n4 = int(input('Digite um número:'))
lista = (n1, n2, n3, n4)
nove = lista.count(9)
print('O número 9 aparece {} vezes'.format(nove))
if lista.count(3) == 0:
    print('O número 3 não foi encontrado nessa lista')
else:
    print('O número 3 apareceu na posição {} da lista'.format(lista.index(3)+1))
print('Os números pares são: ', end='')
for c in range(0, 4):
    if lista[c] % 2 == 0:
        print(lista[c], end=' ' if c < 4 else '\n')
