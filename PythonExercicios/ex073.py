dezprimeiros = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza')
dezultimos = ('São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
vinteprimeiros = dezprimeiros + dezultimos
print('Os times do Campeonato Brasileiro sao: ', end='')
for total in range(0, 20):
    print(vinteprimeiros[total], end=', ' if total < 19 else '.\n')
print('-='*15)
print('Os 5 primeiros colocados são: ', end='')
for cinco in range(0, 5):
    print(vinteprimeiros[cinco], end=', ' if cinco < 4 else '.\n')
print('-=' * 15)
print('Os 4 últimos colocados são: ', end='')
for ultimos in range(-1, -5, -1):
    print(vinteprimeiros[ultimos], end=', ' if ultimos > -4 else '.\n')
print('-='*15)
print('Os times em ordem alfabética são: {}'.format(sorted(vinteprimeiros)))
print('-='*15)
print('O time Bragantino está na {}ª posição'.format(vinteprimeiros.index('Bragantino') + 1))
