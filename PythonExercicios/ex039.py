from datetime import date
atual = date.today().year
ano = int(input('Digite o ano em que você nasceu'))
idade = atual - ano
if idade < 18:
    print('Pode ficar tranquilo! Você ainda tem {} ano(s) para precisar cumprir serviço militar!'.format(18-idade))
elif idade == 18:
    print('Já está na hora de se alistar (caso não o tenha feito ainda)')
else:
    print('Você já passou do tempo de alistamento! Se você não tiver comparecido ao quartel, '
          'corra, pois você está com {} ano(s) de atraso!'.format(idade-18))
