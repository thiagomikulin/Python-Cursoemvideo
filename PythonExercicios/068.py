import random
print('-'*10)
print('PAR OU ÍMPAR')
print('-'*10)
while True:
    jogador = input('Escolha Par ou Ímpar: ').strip().upper()[0]
    while jogador not in 'PI':
        print('Comando inválido! Tente novamente!')
        jogador = input('Escolha Par ou Ímpar').strip().upper()[0]
    if jogador == 'P':
        computador = 'I'
    else:
        computador = 'P'
    n = int(input('Escolha um número: '))
    ncomp = random.randint(0, 10)
    soma = n + ncomp
    if soma % 2 == 0 and jogador in 'P':
        print('-'*15)
        print('PARABÉNS! Você venceu:')
        print('Você escolheu par e a soma resultou em {}'.format(soma))
        print('Vamos jogar novamente?')
        print('-' * 15)
    elif soma % 2 != 0 and jogador in 'I':
        print('-' * 15)
        print('PARABÉNS! Você venceu:')
        print('Você escolheu ímpar e a soma resultou em {}'.format(soma))
        print('Vamos jogar novamente?')
        print('-' * 15)
    elif soma % 2 == 0 and computador == 'P':
        print('-' * 15)
        print('GAME OVER')
        print('Você escolheu ímpar e a soma resultou em {}'.format(soma))
        print('-' * 15)
        break
    elif soma % 2 != 0 and computador == 'I':
        print('-' * 15)
        print('GAME OVER')
        print('Você escolheu par e a soma resultou em {}'.format(soma))
        print('-' * 15)
        break
