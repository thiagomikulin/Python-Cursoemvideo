from utilidadesCeV import moeda, dado

p = dado.leiaDinheiro("Digite um valor: R$")
prop = int(input('Digite a proporção: '))
while True:
    mostrar = input('Deseja mostrar os valores formatados? [S/N]: ').strip().upper()[0]
    if mostrar not in 'SN':
        print('Comando inválido! Tente novamente!')
    else:
        break
if mostrar in 'S':
    show = True
else:
    show = False
moeda.resumo(p, prop, show)
