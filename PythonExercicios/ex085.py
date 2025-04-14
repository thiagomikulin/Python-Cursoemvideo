lista = [[], []]
for c in range(0, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'Os valores pares foram {lista[0]}')
print(f'Os valores ímpares foram {lista[1]}')
print(lista)
