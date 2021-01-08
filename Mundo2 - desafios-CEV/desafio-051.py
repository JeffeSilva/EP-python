#!/usr/bin/env python
print('')
print('{:=^30}'.format (''))
num = int(input('Informe o termo da PA: '))
raz = int(input('Informe a razão da PA: '))
print('{:=^30}'.format (''))
print('')
lim = num + (10 - 1) * raz
for c in range(num, lim + raz, raz):
    print('{}'.format(c), end=' -> ')
print(' FIM ')
print('')
print('{:=^30}'.format (''))
print('')