#Ler expressão e dizer se parênteses abrem e fecham corretamente
#CONTAR PARÊNTESES
#Os parênteses de fechamento APAGAM os de abertura (se ainda tiver, ele dá erro)
lista = []
exp = input('Digite uma expressão: ')
for simb in exp:
    # se for abertura, acrescenta na lista
    if simb == '(':
        lista.append('(')
        #se for fechamento e tiver '(' na lista, remove um, senão adiciona na lista
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão está correta')
else:
    print('A expressão está incorreta')