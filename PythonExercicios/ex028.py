import random
from time import sleep
aleatorio = random.randint(0,5)
print('-=-'*20)
print('Vou pensar em um número de 0 a 5...')
print('-=-'*20)
numero = int(input('Em qual número estou pensando?'))
print("PROCESSANDO...")
sleep(3)
if aleatorio == numero:
    print('!='*20)
    print('Parabéns! Era esse número mesmo!')
    print('!=' * 20)
else:
    print(f'Infelizmente eu pensei no número {aleatorio}! Sinto muito!')
