n1 = int(input('Digite o 1º número'))
n2 = int(input('Digite o 2º número'))
n3 = int(input('Digite o 3º número'))
# Teste de menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Teste de maior
maior = n3
if n2 > n3 and n2 > n1:
    maior = n2
if n1 > n3 and n1 > n2:
    maior = n1

# numeros = [n1, n2, n3]
# sortido = numeros.sort()
# print(sortido)
print('O número {} é o maior e o número {} é o menor'.format(maior, menor))
