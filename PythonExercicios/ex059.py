num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))
opcoes = 0
while opcoes != 5:
    opcoes = int(input('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    Digite uma das opções acima:'''))
    if opcoes == 1:
        print('A soma entre {} e {} é {}'.format(num1, num2, num1+num2))
    elif opcoes == 2:
        print('O número {} vezes o número {} é igual a {}'.format(num1, num2, num1*num2))
    elif opcoes == 3:
        if num1 > num2:
            print('O maior número é {}'.format(num1))
        elif num2 > num1:
            print('O maior número é {}'.format(num2))
        else:
            print('Os dois números são iguais')
    elif opcoes == 4:
        num1 = float(input('Digite um novo número:'))
        num2 = float(input('Digite outro novo número:'))
    elif opcoes >= 6:
        print('Opção inválida! Tente novamente!')
print('Espero ter lhe ajudado!')
