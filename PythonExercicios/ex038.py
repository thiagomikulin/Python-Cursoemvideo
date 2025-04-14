n1 = float(input('Escreva um número'))
n2 = float(input('Escreva outro número'))
if n1 > n2:
    print('O valor {} é maior que o valor {}'.format(n1, n2))
elif n1 < n2:
    print('O valor {} é maior que o valor {}'.format(n2, n1))
else:
    print('Não existe valor maior. Os dois são iguais!')