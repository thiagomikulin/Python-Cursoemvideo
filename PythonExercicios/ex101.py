def voto(num):
    import datetime
    """
    Define se uma pessoa pode votar
    :param num: ano de nascimento
    :return: Valor da idade e se a pessoa poderá votar
    """
    idade = datetime.date.today().year - num
    if idade < 16:
        return f"Com {idade} anos, seu voto é NEGADO"
    elif 16 <= idade < 18 or idade >= 65:
        return f"Com {idade} anos, seu voto é OPCIONAL"
    else:
        return f"Com {idade} anos, seu voto é OBRIGATÓRIO"


print(voto(int(input('Digite o seu ano de nascimento: '))))
