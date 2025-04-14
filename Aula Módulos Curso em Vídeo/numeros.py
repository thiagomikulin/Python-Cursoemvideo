from uteis import numeros
num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'''O fatorial de {num} é {fat}
O dobro de {num} é {numeros.dobro(num)}
O triplo de {num} é {numeros.triplo(num)}''')