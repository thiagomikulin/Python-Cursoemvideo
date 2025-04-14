itotal = 0
imedia = 0
maior = 0
nomemaior = ''
menosde20 = 0
for p in range(1,5):
    nome = input('Qual é o seu nome?')
    idade = float(input('Quantos anos você tem?'))
    sexo = input('Você é Homem [ H ] ou Mulher [ M ]? ').upper()
    itotal += idade
    if p == 1 and sexo == 'H':
        maior = idade
    else:
        if idade > maior and sexo == 'H':
            maior = idade
            nomemaior = nome
    if idade < 20 and sexo == 'M':
        menosde20 += 1
imedia = itotal / 4
print('A media de idade do grupo é de {:.1f} anos'.format(imedia))
print('O homem mais velho tem {:.0f} anos e se chama {}'.format(maior, nomemaior))
print('No total, tem-se {} mulheres com menos de 20 anos'.format(menosde20))
