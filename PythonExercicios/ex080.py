maior = menor = meio = cont = 0
lista = []
while cont < 5:
    num = int(input('Digite um número: '))
    if cont == 0 or num > lista[-1]:
        maior = num
        menor = num
        lista.append(num)
        print('Número inserido no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
    cont += 1
print(lista)
#Dupla verificação para conferência (1 quando coloca na lista, outra pra comparar números posteriores um a um até alcançar número-alvo
