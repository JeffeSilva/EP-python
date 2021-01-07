#!/usr/bin/env python
print(' ')
print('{:=^30}'.format (''))
print(' ')
valores = 0
for c in range(0, 6):
    num = int(input('Informe seis valores: '))
    if num % 2 == 0:
        valores = valores
    else:
        valores = valores + num
print(' ')
print('A soma somente dos números impares é: {}'.format(valores))
print(' ')
print('{:=^30}'.format (''))