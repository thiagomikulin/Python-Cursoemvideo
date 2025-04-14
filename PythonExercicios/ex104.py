def leiaInt(num):
    while num.isnumeric() == False:
            print('\033[1;31mComando inválido! Tente novamente!\033[m')
            num = input('Digite um número: ')
    print(f'O valor lido foi {num}')


n = leiaInt(input('Digite um número: '))