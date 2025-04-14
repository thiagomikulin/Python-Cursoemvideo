aluno = {}
aluno['nome'] = input('Nome do aluno: ')
nota1 = float(input('Digite a 1ª nota do aluno: '))
nota2 = float(input('Digite a 2ª nota do aluno: '))
aluno['media'] = (nota1 + nota2) / 2
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
elif aluno['media'] < 3:
    aluno['situação'] = 'REPROVADO'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
