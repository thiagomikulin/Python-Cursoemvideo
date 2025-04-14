valor = float(input('Escreva o preço do produto'))
desconto = valor / 100 * 5
print('O valor do produto de R${:.2f} com um desconto de 5% será de R${:.2f}'.format(valor, valor - desconto))

