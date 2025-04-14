def titulo(msg):
    print('-' * 40)
    print(f'\033[32m{msg:^40}\033[m')
    print('-' * 40)

def linha(msg):
    print('-' * 40)

def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[35m{item}\033[m')
        c += 1

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mComando inválido! Tente novamente!\033[m')
            continue
        else:
            return num
            break

