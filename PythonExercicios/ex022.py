nome = input('Digite seu nome:').strip()
nomesemespaco = nome.replace(" ", "")
print('O seu nome em letras maiúsculas é: {} \nO seu nome com letras minúsculas é: {} \nO nome tem {} letras \nO primeiro nome tem {} letras'.format(nome.upper(), nome.lower(), len(nomesemespaco), nome.split()[0].__len__()))

