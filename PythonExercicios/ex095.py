jogadores = []
while True:
    jogador = {
        "nome": input('Nome do jogador: '),
        "gols": []
    }
    total = 0
    partidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou: '))
    for g in range(0, partidas):
        gols = int(input(f'Quantos gols o jogador fez na partida {g + 1}: '))
        total += gols
        jogador['gols'].append(gols)
    jogador['total'] = total
    jogadores.append(jogador.copy())
    mais = input('Deseja registrar mais algum jogador? [S/N]').upper().strip()[0]
    if mais in 'N':
        break
while True:
    print('=-' * 30)
    for c in range(0, len(jogadores)):
        print(f'{c} --> {jogadores[c]}')
    print('=-' * 30)
    dados = int(input('Deseja saber as estatísticas de qual jogador [999 para parar]? --> '))
    while dados > len(jogadores):
        print('Esse jogador não está registrado! Tente novamente')
        dados = int(input('Deseja saber as estatísticas de qual jogador [999 para parar]? --> '))
    if dados == 999:
        break
    for i, v in jogadores[dados].items():
        print(f'O campo {i} tem o valor {v}.')
    print('=-' * 30)
    print(f'O jogador {jogadores[dados]["nome"]} jogou {jogadores[dados]["gols"].__len__()} partidas.')
    for i, v in enumerate(jogadores[dados]["gols"]):
        print(f'==>Na partida {i}, fez {v} gols')
    print(f'Foi um total de {jogadores[dados]["total"]} gols')
print('ENCERRANDO...')
print('Obrigado! Tenha um bom dia!')
