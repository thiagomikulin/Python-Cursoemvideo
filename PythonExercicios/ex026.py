frase = input('Escreva uma frase').strip()
contadorA = frase.lower().count('a')
primeiroA = frase.lower().find('a') +1
ultimoA = frase.lower().rfind('a') +1
print('A frase que você digitou tem {} letras "A"\nA primeira está na posição {}\nE a última está na posição {}'.format(contadorA, primeiroA, ultimoA))
