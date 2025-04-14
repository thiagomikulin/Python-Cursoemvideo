lista = []
def calculoMaior(*num):
    print(f'Da lista {sorted(lista)}, o maior valor foi {sorted(lista)[-1]}')


while True:
    num = int(input('Insira um número: '))
    lista.append(num)
    while True:
        mais = input('Quer continuar? [S/N] --> ').strip().upper()[0]
        if mais not in 'SN':
            print('Comando inválido! Tente novamente!')
        else:
            break
    if mais in 'N':
        break
calculoMaior(lista)

