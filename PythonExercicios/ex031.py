distancia = float(input('Digite a distância da sua viagem:'))
if distancia <= 200:
    tarifa = distancia * 0.5
else:
    tarifa = distancia * 0.45
print('A sua viagem custará R${:.2f}'.format(tarifa))
