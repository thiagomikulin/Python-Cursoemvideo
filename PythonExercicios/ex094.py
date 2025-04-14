pessoas = []
pessoa = {}
soma = 0
mulheres = []
acima = []
while True:
    pessoa.clear()
    pessoa["Nome"] = input('Nome: ')
    while True:
        pessoa["sexo"] = input('Sexo [M/F]: ').strip().upper()[0]
        if pessoa["sexo"] not in 'MF':
            print('Comando inválido!')
        else:
            if pessoa["sexo"] in 'F':
                mulheres.append(pessoa["Nome"])
            break
    pessoa["idade"] = int(input('Idade: '))
    soma += pessoa["idade"]
    pessoas.append(pessoa.copy())
    mais = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if mais not in 'SN':
        print('Comando inválido!')
        mais = input('Deseja continuar [S/N]? ').strip().upper()[0]
    elif mais in "N":
        break
print(pessoas)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'A média da idade de todos é de {soma / len(pessoas):5.2f} anos')
if mulheres == []:
    print('Não foi registrada nenhuma mulher!')
else:
    print(f'Ao todo, tivemos {len(mulheres)} mulheres, e elas são: {mulheres}')
for c in pessoas:
    if c["idade"] > soma / len(pessoas):
        acima.append(c["Nome"])
print(f"As pessoas acima da média de idade são: {acima}")
