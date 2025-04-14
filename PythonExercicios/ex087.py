lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input('Digite o valor para [{},{}]: '.format(l, c)))
        if num % 2 == 0:
            pares += num
        if c == 2:
            coluna += num
        if l == 1 and c == 0:
            maior = num
        else:
            if lista[l][1] > maior:
                maior = num
        lista[l][c] = num
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {lista[l][c]:^3}  ]', end='')
    print()
print(f'A soma de todos os valores pares é {pares}')
print(f'A soma dos valores na terceira coluna é {coluna}')
print(f'O maior valor da 2ª linha é {maior}')
