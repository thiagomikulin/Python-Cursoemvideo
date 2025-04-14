numeros = []
for c in range(0,5):
    numeros.append(int(input('Digite um número: ')))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print(f'A lista conteve os números: {numeros}')
print(f'O maior valor da lista foi {maior}, nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}...', end='')
print('\n')
print(f'O menor valor da lista foi {menor}, nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...', end='')
print('\n')