pessoas = []
maispesado = maisleve = 0
while True:
    nome = input('Digite um nome: ')
    peso = float(input('Digite quanto essa pessoa pesa: '))
    individuo = [nome, peso]
    if len(pessoas) == 0:
        maispesado = maisleve = individuo[1]
    else:
            if individuo[1] > maispesado:
                maispesado = individuo[1]
            if individuo[1] < maisleve:
                maisleve = individuo[1]
    pessoas.append(individuo[:])
    mais = input('Quer continuar? [S/N]').upper().strip()[0]
    if mais not in 'SN':
        print('Erro! Comando inválido! Tente novamente!')
        mais = input('Quer continuar? [S/N]').upper().strip()[0]
    elif mais in 'N':
        break
print('Um total de {} pessoas foram cadastradas'.format(len(pessoas)))
print(f'O maior peso foi de {maispesado} Kg: ', end='')
for p in pessoas:
    if p[1] == maispesado:
        print(f'{p[0]}...', end='')
print(f'\nO menor peso foi de {maisleve} Kg: ', end='')
for l in pessoas:
    if l[1] == maisleve:
        print(f'{l[0]}...', end='')
#Nunca esqueça que os valores podem ser lidos em qualquer ordem, não necessariamente quando eles chegam/são criados
#A não ser que sejam modificados