total = 0
maisdemil = 0
maisbarato = ''
precomaisbarato = 0
cont = 0
print('-'*10)
print('MERCADO DE CONSULTA')
while True:
    print('-' * 10)
    produto = input('Qual é o nome do produto? ').capitalize()
    preço = float(input('Qual é o preço desse produto? R$'))
    total += preço
    if preço > 1000:
        maisdemil += 1
    if cont == 0:
        maisbarato = produto
        precomaisbarato = preço
    else:
        if preço < precomaisbarato:
            preço = precomaisbarato
            maisbarato = produto
    cont += 1
    mais = input('Deseja inserir mais produtos [S/N]? ').strip().upper()[0]
    if mais in 'N':
        break
    elif mais not in 'S':
        print('ERRO! Comando inválido! Tente novamente!')
        mais = input('Deseja inserir mais produtos [S/N]? ').strip().upper()[0]
print('''O total de todos os valores dá R${:.2f}
{} produtos custam mais de R$1000,00
O produto {} é o mais barato'''.format(total, maisdemil, maisbarato))
