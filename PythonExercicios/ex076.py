produtos1 = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20)
produtos2 = ('Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
produtos = produtos1 + produtos2
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
for c in range(0, 18):
    if c % 2 == 0:
        print('{:.<30}R$'.format(produtos[c]), end='')
    else:
        print('{:>7.2f}'.format(produtos[c]), end='\n')
