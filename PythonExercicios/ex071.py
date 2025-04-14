cinquenta = vinte = dez = um = 0
dinheiro = int(input('Quanto você pretende sacar?'))
while dinheiro >= 50:
    cinquenta += 1
    dinheiro -= 50
while dinheiro >= 20:
    vinte += 1
    dinheiro -= 20
while dinheiro >= 10:
    dez += 1
    dinheiro -= 10
while dinheiro > 0:
    um += 1
    dinheiro -= 1
print('Você irá sacar:')
if cinquenta > 0:
    print('{} notas de R$50'.format(cinquenta))
if vinte > 0:
    print('{} notas de R$20'.format(vinte))
if dez > 0:
    print('{} notas de R$10'.format(dez))
if um > 0:
    print('{} notas de R$1'.format(um))
