import random
print('- '*30)
print('\033[1;34;40mBem vindo ao Jokenpô!\033[m')
print('\033[1;34;40mPara esse jogo, você escolherá números que irão representar cada mão')
print('\033[1;34;40mPara pedra - 1; Para papel - 2; Para tesoura - 3')
jogador1 = int(input('Por favor,digite um dos números acima: '))
jogador2 = random.randint(1,3)
if jogador1 > 3:
    print('Por favor, digite um dos valores solicitados')
else:
    if jogador1 == jogador2:
        print('Empatamos! Vamos tentar de novo?')
    else:
        if jogador1 == 1 and jogador2 == 2:
            print('VENCI! Você escolheu pedra e eu escolhi papel!')
        elif jogador1 == 1 and jogador2 == 3:
            print('PARABÉNS! VOCÊ VENCEU! Eu escolhi tesoura e você escolheu pedra')
        elif jogador1 == 2 and jogador2 == 1:
            print('PARABÉNS! VOCÊ VENCEU! Eu escolhi pedra e você escolheu papel')
        elif jogador1 == 2 and jogador2 == 3:
            print('VENCI! Você escolheu papel e eu escolhi tesoura!')
        elif jogador1 == 3 and jogador2 == 1:
            print('VENCI! Você escolheu tesoura e eu escolhi pedra!')
        elif jogador1 == 3 and jogador2 == 2:
            print('PARABÉNS! VOCÊ VENCEU! Eu escolhi papel e você escolheu tesoura')
