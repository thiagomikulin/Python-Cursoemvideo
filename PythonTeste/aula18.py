teste = list()
teste.append('Thiago')
teste.append(24)
galera = list()
galera.append(teste[:])
teste[0] = "Gustavo"
teste[1] = 40
galera.append(teste[:])
print(galera)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
