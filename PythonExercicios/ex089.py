aluno = []
lista = []
while True:
    if len(aluno) > 0:
        del (aluno[0:4])
    aluno.append(str(input('Nome do aluno: ')))
    aluno.append(float(input('Digite a 1ª nota: ')))
    aluno.append(float(input('Digite a 2ª nota: ')))
    media = (aluno[1] + aluno[2]) / 2
    aluno.append(media)
    lista.append(aluno[:])
    mais = input('Quer continuar? [S/N]').upper().strip()[0]
    if mais not in 'SN':
        print('Comando inválido! Tente novamente!')
        mais = input('Quer continuar? [S/N]').upper().strip()[0]
    elif mais in 'N':
        break
for c in range(0, len(lista)):
    print('{} - Aluno: {:.<30}Média: {:.1f}'.format(c + 1, lista[c][0], lista[c][3]))
while True:
    qual = int(input('De qual aluno você gostaria de saber a nota? [999 para fechar]'))
    if qual == 999:
        break
    print('{} - Aluno: {}/ n1: {}/ n2: {}'.format(qual, lista[qual - 1][0], lista[qual - 1][1], lista[qual - 1][2]))
print('FINALIZANDO! Tenha um ótimo dia!')
