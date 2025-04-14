import random
nome1 = input('Nome do 1º aluno')
nome2 = input('Nome do 2º aluno')
nome3 = input('Nome do 3º aluno')
nome4 = input('Nome do 4º aluno')
nomes = [nome1, nome2, nome3, nome4]
randomize = random.sample(nomes, 4)
print('A ordem das apresentações será: {}'.format(randomize))
