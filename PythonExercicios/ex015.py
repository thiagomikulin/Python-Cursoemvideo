dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
precoDias = dias * 60
precoKm = km * 0.15
total = precoDias + precoKm
print('O total a ser pago será de R${:.2f}'.format(total))
