print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
l1 = int(input('Digite o 1º lado:'))
l2 = int(input('Digite o 2º lado:'))
l3 = int(input('Digite o 3º lado:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Essas medidas podem formar um triângulo')
    if l1 == l2 == l3:
        print('Este é um triângulo equilátero')
    elif l1 != l2 != l3:
        print('Este é um triângulo escaleno')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('Este é um triângulo isósceles')
else:
    print('Essas medidas não formam um triângulo')
