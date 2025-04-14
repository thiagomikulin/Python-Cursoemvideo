def fatorial(num, show=False):
    """
    Função para calcular fatorial de um número
    :param num: O número a ser calculado
    :param show: A opção de mostrar a conta completa (ou não)
    :return: O valor do fatorial de num
    """
    for c in range(num, 0, -1):
        if c < num:
            num *= c
        if fatorial(show):
            print(f'{c}', end=' X ' if c > 1 else ' = ')
    return num


print(fatorial(5, show=True))

