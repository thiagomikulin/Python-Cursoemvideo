import math
catetoOposto = float(input('Digite o cateto oposto'))
catetoAdjacente = float(input('Digite o cateto adjacente'))
soma = (catetoOposto ** 2) + (catetoAdjacente ** 2)
raiz = math.sqrt(soma)
print('A medida da hipotenusa é de {:.2f}'.format(raiz))
