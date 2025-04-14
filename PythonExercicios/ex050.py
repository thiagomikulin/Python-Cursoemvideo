soma = 0
for numeros in range(0, 6, 1):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma += num
print(soma)
