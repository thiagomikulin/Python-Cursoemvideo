lista = []
while True:
    n = int(input('Digite um número:'))
    if n in lista:
        print('Esse número já está na lista...Não vou acrescentar.')
    else:
        lista.append(n)
    mais = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if mais not in 'SN':
        print('Comando inválido! Tente novamente!')
        mais = input('Deseja continuar? [S/N] ').upper().strip()[0]
    elif mais in 'N':
        break
lista.sort()
print(f'A lista, escrita em ordem crescente, é: {lista}')