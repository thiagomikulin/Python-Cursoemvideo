from random import randint
print('-'*15)
print(' '*10, 'PAR OU ÍMPAR')
print('-'*15)
while True:
    escolha = input('Par ou ímpar [P/I]? ').strip().upper()[0]
    if escolha not in 'PI':
        print('Erro! Comando Inválido! Tente novamente!')
        escolha = input('Par ou ímpar [P/I]? ').strip().upper()[0]
    else:
        if escolha in 'P':
            computador = 'I'
        else:
            computador = 'P'
    num = int(input('Escolha um número: '))
    numcomp = randint(0, 10)
    soma = num + numcomp
    if soma % 2 == 0 and escolha == 'P' or soma % 2 != 0 and escolha == 'I':
        print('PARABÉNS! Você venceu!')
        print('A soma deu {} e você escolheu {}'.format(soma, escolha))
    else:
        print('GAME OVER')
        print('A soma deu {} e você escolheu {}'.format(soma, escolha))
        break
