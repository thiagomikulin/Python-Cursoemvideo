soma = 0
cont = 0
for calculo in range(1, 501, 2):
    if calculo % 3 == 0:
        soma += calculo
        cont += 1
print(soma, cont)
