from time import sleep
def contador(ini, fim, passo):
    if passo == 0:
        passo = 1
    print(f'CONTANDO DE {ini} ATÉ {fim} EM PASSO {passo}')
    for c in range(ini, fim+1 if ini < fim else fim-1, passo):
        sleep(0.5)
        print(f'{c} -->', end=' ')
    sleep(0.5)
    print('FIM')
    print('-'*30)


contador(1, 10, 1)
contador(10, 0, -2)
novoini = int(input('Digite um valor para início: '))
novofim = int(input('Digite um valor para fim: '))
novopasso = int(input('Digite um valor para passo: '))
if novopasso == 0 and novoini > novofim:
    novopasso = -1
if novoini > novofim and novopasso > 0:
    novopasso = -novopasso
contador(novoini, novofim, novopasso)
