from random import randint
from time import sleep
lista = []
def sorteia(*num):
    for c in range(0, 5):
        num = randint(0, 1000)
        lista.append(num)
    print(f'Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        print(f'{lista[c]}', end=', ' if c < 4 else ' =-=-= ')
        sleep(0.3)
    print('PRONTO!')
def somaPar():
    soma = 0
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            soma += lista[c]
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia()
somaPar()
