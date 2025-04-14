def ficha(nome='<desconhecido>', gols=0):
    """
    Define as estatísticas do jogador
    :param nome: Nome do jogador
    :param gols: número de gols
    :return: Valores em texto (caso não preenchido, voltam valores opcionais)
    """
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'

n = input('Nome do jogador: ')
g = input('Número de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    print(ficha(gols=g))
else:
    print(ficha(n, g))
#você fez com len antes (é válido, mas não tem a mesma proposta do g)