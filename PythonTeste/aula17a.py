num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(0, 3)
num.sort()
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na opsição {c} encontrei o número {v}')
print(f'Cheguei ao fim da lista')