lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    mais = input('Deseja continuar? [S/N]').upper().strip()
    if mais not in 'SN':
        print('Comando inválido! Tente novamente!')
        mais = input('Deseja continuar? [S/N]').upper().strip()
    elif mais in 'N':
        break
lista.sort()
print(f'''O total de números digitados foi {len(lista)}
Os números em ordem descrescente são: {lista[::-1]}''')
if lista.count(5) == 0:
    print('O número 5 não está na lista')
else:
    print(f'O número 5 está na lista e foi digitado {lista.count(5)} vezes')
