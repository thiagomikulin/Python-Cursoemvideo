n = int(input('Digite o quanto de números da Sequễncia de Fibonacci deseja ver? -->'))
cont = 3
t1 = 0
t2 = 1
if n == 1:
    print('{} --> '.format(t1), end='')
elif n >= 2:
    print('{} --> {} --> '.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print('{} --> '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
