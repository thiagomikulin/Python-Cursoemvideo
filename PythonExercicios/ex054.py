import datetime
maiores = 0
menores = 0
atual = datetime.date.today().year
for anos in range (0, 7, 1):
    ano = int(input('Digite um ano de nascimento'))
    idade = atual - ano
    if idade < 18:
        maiores += 1
    else:
        menores += 1
print('{} pessoas já atingiram a maioridade, enquanto {} ainda não atingiram'.format(maiores, menores))


