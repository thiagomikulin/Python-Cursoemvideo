velocidade = int(input('Digite sua velocidade:'))
if velocidade > 80:
    multa = float((velocidade - 80) * 7)
    print('Você foi multado e terá que pagar um valor de R${:.2f}'.format(multa))
else:
    print('Tudo regularizado, chefia!')