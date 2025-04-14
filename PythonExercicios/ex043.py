import time
peso = float(input('Digite o seu peso:'))
alt = float(input('Digite a sua altura:'))
imc = peso / alt ** 2
print('Calculando...')
time.sleep(3)
print('O seu IMC (Índice de Massa Corporal) é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso!')
elif 18.5 < imc <= 25:
    print('Você está no peso ideal')
elif 25 < peso <= 30:
    print('Você está com sobrepeso')
elif 30 < peso <= 40:
    print('Você se enquadra no quadro de Obesidade')
else:
    print('Você se enquadra em Obesidade Mórbida')
