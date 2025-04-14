def area(larg, comp):
    a = larg * comp
    print('-~'*30)
    print(f'A área do terreno é de {a}m²')

def titulo(t):
    print('-'*30)
    print(t)
    print('-' * 30)


titulo('CALCULADOR DE ÁREA')
largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area(largura, comprimento)
