termo = int(input('Digite um número (como termo): '))
razao = int(input('Digite a razão da PA: '))
cont = 10
#FÓRMULA DO ENÉSIMO TERMO DE PA
while cont > 0:
    print('{}'.format(termo), end='')
    print(' --> ' if cont > 1 else ' ==FIM== ', end='')
    termo += razao
    cont -= 1
