from time import sleep
from random import randint
computer = randint(0,10)
tentativas = 0
print('-=-'*20)
print('Vou pensar em um número de 0 a 10...')
print('-=-'*20)
numero = int(input('Em qual número estou pensando?'))
while numero != computer:
    if computer > numero:
        print('Mais... Tente novamente!')
    elif computer < numero:
        print('Menos... Tente novamente')
    numero = int(input('Em qual número estou pensando?'))
    tentativas += 1
if numero == computer:
    print('PARABÉNS! Você acertou o número em {} tentativas!'.format(tentativas+1))
