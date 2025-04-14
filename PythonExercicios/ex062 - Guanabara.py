print('GERADOR DE PA')
print('-='*10)
primeiro = int(input('Digite um número (como termo): '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
#FÓRMULA DO ENÉSIMO TERMO DE PA
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} --> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Foram mostrados {} termos no total'.format(total))
print('FIM')
