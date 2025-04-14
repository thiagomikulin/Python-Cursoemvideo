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
print('=-' * 30)
print(jogador)
print('=-' * 30)
for i, v in jogador.items():
    print(f'O campo {i} tem o valor {v}.')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["gols"].__len__()} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'==>Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')