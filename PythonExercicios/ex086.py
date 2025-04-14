lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input('Digite o valor para [{},{}]: '.format(l, c)))
        lista[l][c] = num
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {lista[l][c]:^5}  ]', end='')
    print()
