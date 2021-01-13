#!/usr/bin/env python
num = int(input('Informe quantos termos deseja: '))
n1 = 0
n2 = 1
c = 2
print('{} -> {}'.format(n1, n2), end='')
while c < num:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    c += 1
    print(' -> {}'.format(n3), end='')
print(' -> FIM')  