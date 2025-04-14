zeroaavinte = ('zero', 'um', 'dois', 'três', 'quatro',
               'cinco', 'seis', 'sete', 'oito', 'nove',
               'dez', 'onze', 'doze', 'treze', 'quatorze',
               'quinze', 'dezesseis', 'dezessete', 'dezoito',
               'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
while n not in range(0, 21):
    print('Erro! Comando inválido! Tente novamente')
    n = int(input('Digite um número entre 0 e 20: '))
print('Você digitou o número {}'.format(zeroaavinte[n]))
#DICA: Concatene variáveis para não estender demais