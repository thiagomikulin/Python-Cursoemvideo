salario = float(input('Digite o seu salário'))
if salario > 1250:
    aumento = salario / 100 * 10
    print('O seu aumento foi de R${:.2f}'.format(aumento))
else:
    aumento = salario / 100 * 15
    print('O seu aumento foi de R${:.2f}'.format(aumento))
