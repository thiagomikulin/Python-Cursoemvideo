pali = input('Digite uma frase: ').lower()
divide = pali.split()
junto = ''.join(divide)
inverso = ''

#é -1 porque a contagem de letras começa no 0, não no 1 (diferente do len)
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('\nEssa palavra é um palíndromo')
else:
    print('\nEssa frase não é um palíndromo')
