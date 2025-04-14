def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mComando inválido! Tente novamente!\033[m')
            continue
        except KeyboardInterrupt:
            print('\nO usuário decidiu não declarar o valor!')
            print(f'O número inteiro digitado foi 0')
            break
        else:
            print(f'O número inteiro digitado foi {num}')
            break

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            print('\033[1;31mComando inválido! Tente novamente!\033[m')
        except KeyboardInterrupt:
            print('O usuário decidiu não declarar o valor!')
            print(f'O número real digitado foi 0')
        else:
            print(f'O número real digitado foi {num}')

leiaInt('Digite um número inteiro: ')
leiaFloat('Digite um número real: ')