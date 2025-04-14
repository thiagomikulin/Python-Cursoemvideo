maior = 0
homens = 0
mulhermenor = 0
while True:
    print('-' * 15)
    print('NOVO REGISTRO')
    print('-'*15)
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulhermenor += 1
    mais = input('Quer continuar [S/N]? ').strip().upper()[0]
    if mais in 'N':
        break
print('''No total, foram registradas {} pessoas com mais de 18 anos
Um total de {} homens foram cadastrados
{} mulheres com menos de 20 anos foram cadastradas'''.format(maior, homens, mulhermenor))
