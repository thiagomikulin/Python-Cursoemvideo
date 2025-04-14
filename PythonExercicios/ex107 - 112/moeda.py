def aumentar(num, proporcao, show=True):
    aumento = num / 100 * proporcao
    if show == True:
        return moeda(num + aumento)
    else:
        return num + aumento


def diminuir(num, proporcao, show=True):
    diminuicao = num / 100 * proporcao
    if show == True:
        return moeda(num - diminuicao)
    else:
        return num - diminuicao

def dobro(num, show=True):
    if show == True:
        return moeda(num * 2)
    else:
        return num * 2

def metade(num, show=True):
    if show == True:
        return moeda(num / 2)
    else:
        return num / 2

def moeda(num):
    return f'R${num:.2f}'

def resumo(num, proporcao, show=True):
    print('-' * 30)
    print(f'      RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: {moeda(num):>10}')
    print(f'Dobro do preço: {dobro(num, show):>11}')
    print(f'Metade do preço: {metade(num, show):>10}')
    print(f'{proporcao}% de aumento: {aumentar(num, proporcao, show):>11}')
    print(f'{proporcao}% de redução: {diminuir(num, proporcao, show):>11}')
    print('-' * 30)
