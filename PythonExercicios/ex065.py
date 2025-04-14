soma = 0
cont = 0
mais = 0
maior = 0
menor = 0
while mais != 1:
    num = int(input('Digite um valor:'))
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    print('''A média de todos os valores é de {}
O maior valor lido foi {}
O menor valor lido foi {}'''.format(soma/cont, maior, menor))
    mais = int(input('Opções: \n[ 0 - Sim ] \n[ 1 - Não ]\nDeseja digitar mais valores?: '))
