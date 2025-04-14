soma = cont = 0
while True:
    n = int(input('Digite um número (999 para parar)'))
    if n == 999:
        break
    cont += 1
    soma += n
print('Você digitou {} valores e a soma de todos eles é {}'.format(cont, soma))
