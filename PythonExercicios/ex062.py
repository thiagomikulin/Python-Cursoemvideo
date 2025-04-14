termo = int(input('Digite um número (como termo): '))
razao = int(input('Digite a razão da PA: '))
cont = 1
novo = 10
while novo != 0:
    formnovo = cont + novo
    if novo == 10:
        while cont <= novo:
                print('{}'.format(termo), end='')
                print(' --> ' if cont < novo else '==FIM==\n', end='')
                cont += 1
                termo += razao
        novo = int(input('Deseja saber mais quantos termos?'))
    else:
        while cont < formnovo:
            print('{}'.format(termo), end='')
            print(' --> ' if cont < formnovo else '==FIM==\n', end='')
            cont += 1
            aumento = 1
            termo += (razao * aumento)
            aumento += 1
        novo = int(input('Deseja saber mais quantos termos? (Digite 0 para finalizar): '))
