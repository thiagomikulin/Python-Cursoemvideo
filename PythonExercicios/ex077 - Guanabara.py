palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p}, temos: ', end='')
    for letra in p:
        #Não esqueça que você tentou esse método, mas desistiu cedo demais
        if letra.lower() in 'aeiou':
            print(letra, end=' ')