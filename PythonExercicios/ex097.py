
def escreva(texto):
    maior = len(texto) + 4
    print('-' * maior)
    print(f'  {texto}')
    print('-' * maior)


mensagem = input('Escreva uma mensagem: ')
escreva(mensagem)