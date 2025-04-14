valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos você pretende pagar:'))
porcentagem = salario * 30 / 100
prestacao = valor / (anos * 12)
if prestacao <= porcentagem:
    print('Parabéns! O seu salário de R${:.2f} é suficiente para cobrir as prestações de R${:.2f}'.format(salario, prestacao))
    print('A casa poderá ser quitada em {:.0f} anos com as prestações mensais de R${:.2f}'.format(anos, prestacao))
else:
    print('Infelizmente, o seu salário de R${:.0f} não é suficiente para pagar as prestações mensais de R${:.2f}'.format(salario, prestacao))
