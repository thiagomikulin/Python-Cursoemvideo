


while True:
    ajuda = input('Digite o comando [Digite FIM para finalizar]: ')
    if ajuda in 'FIM':
        break
    print("\033[7;38m")
    print(help(ajuda))
    print('\033[m')

