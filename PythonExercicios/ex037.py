numero = int(input('Digite um número inteiro:'))
base = int(input('''Escolha uma dessas bases de conversão:
[ 1 ] - Binário
[ 2 ] - Octal
[ 3 ] - Hexadecimal
Digite sua escolha:'''''))

if base == 1:
    print('O valor {} convertido em binário é: {}'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('O valor {} convertido em octal é: {}'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('O valor {} convertido em hexadecimal é: {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida! Tente novamente')
