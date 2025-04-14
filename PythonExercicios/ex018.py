import math
grau = float(input('Escreva um ângulo'))
grauradiano = math.radians(grau)
seno = math.sin(grauradiano)
cosseno = math.cos(grauradiano)
tangente = math.tan(grauradiano)
print('Para o valor {:.0f} graus, {:.2f} é o seno, {:.2f} é o cosseno e {:.2f} é a tangente'.format(grau, seno, cosseno, tangente))
