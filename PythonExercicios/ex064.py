cont = 0
soma = 0
num = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]:'))
    cont += 1
    soma += num
print('Você digitou {} números e a soma de todos eles dá {}'.format(cont - 1, soma - 999))
