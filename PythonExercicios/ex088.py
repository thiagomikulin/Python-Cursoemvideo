from random import randint
from time import sleep
palp = int(input('Quantos palpites você quer? '))
lista = []
cont = 1
while True:
    sleep(1)
    for numeros in range(1, 7):
        num = randint(1, 60,)
        if num not in lista:
            lista.append(num)
        else:
            num = randint(1, 60)
            lista.append(num)
    lista.sort()
    print('Jogo {}: {}'.format(cont, lista[:]))
    cont += 1
    del lista[0:6]
    if cont == palp+1:
        break
