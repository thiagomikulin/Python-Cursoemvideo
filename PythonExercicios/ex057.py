genero = input('Digite M se você for homem e F se for mulher: ').upper().strip()[0]
while genero not in 'MmFf':
    print('Gênero Inválido! Tente novamente')
    genero = input('Digite M se você for homem e F se for mulher: ').upper().strip()[0]
print('genero {} registrado!'.format(genero))

