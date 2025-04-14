lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    mais = input('Deseja digitar mais algum valor? [S/N] ').upper().strip()[0]
    if mais not in 'SN':
        print('Comando inválido! Tente novamente!')
        mais = input('Deseja digitar mais algum valor? [S/N] ').upper().strip()[0]
    elif mais in 'N':
        break
pares = []
impares = []
for pos in range(0, len(lista)):
    if lista[pos] % 2 == 0:
        pares.append(lista[pos])
    else:
        impares.append(lista[pos])
impares.sort()
pares.sort()
lista.sort()
print(f'A lista sem divisão é: {lista}\nA lista apenas com os pares é: {pares}\nA lista apenas com os ímpares é: {impares}')
