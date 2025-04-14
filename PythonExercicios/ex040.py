nota = float(input('Digite a sua nota: '))
if nota <= 5.0:
    print('REPROVADO')
elif 5.0 < nota <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
