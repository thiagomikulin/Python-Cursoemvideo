def notas(alunos, quant, situacao=False):
    """
    Define a situação da turma com base de análise de lista/dicionário
    :param alunos: Os dados gerais da turma
    :param situacao: Define a situação geral da turma com base nos dados
    :return: A quantidade de notas, a maior e menor nota, a média da turma e a situação
    """
    global menor, maior
    quant = len(alunos)
    soma = 0
    for n in range(0, len(alunos)):
        soma += alunos[n]["nota"]
        if n == 0:
            maior = alunos[n]["nota"]
            menor = alunos[n]["nota"]
        else:
            if alunos[n]["nota"] > maior:
                maior = alunos[n]["nota"]
            if alunos[n]["nota"] < menor:
                menor = alunos[n]["nota"]
    media = soma / len(alunos)
    print(f'''A quantidade de notas da turma é {quant}
A maior nota da turma foi {maior}
A menor nota da turma foi {menor}
A média geral da turma foi {media}''')
    if situacao == True:
        if media >= 7:
            print('A situação da turma é: BOA')
        elif 5 <= media < 7:
            print('A situação da turma é: RAZOÁVEL')
        else:
            print('A situação da turma é: RUIM')
#Ao invés de maior e menor, era possível usar max() e min()


#Programa principal
turma = []
while True:
    aluno = {}
    aluno.clear()
    aluno["nome"] = input('Nome do Aluno: ')
    aluno["n1"] = float(input('N1: '))
    aluno["n2"] = float(input('N2: '))
    aluno["nota"] = (aluno["n1"] + aluno["n2"]) / 2
    turma.append(aluno)
    mais = input('Deseja registrar mais alunos? [S/N]: ').upper().strip()[0]
    while True:
        if mais not in 'SN':
            print("Comando inválido! Tente novamente!")
            mais = input('Deseja registrar mais alunos? [S/N]: ').upper().strip()[0]
        else:
            break
    if mais in 'N':
        break
print('Temos o resultado da turma!')
while True:
    sit = input('Você gostaria de saber a situação da turma? [S/N]: ').upper().strip()[0]
    if sit not in 'SN':
        print('Comando inválido! Tente novamente!')
    else:
        break
if sit in 'S':
    notas(turma, len(turma), True)
    #Essa solução em lista fica melhor (com *num, ele não reconhece a situação sem digitar "situacao")
else:
    notas(turma, len(turma))
