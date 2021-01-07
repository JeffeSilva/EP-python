#!/usr/bin/env python
print('')
print('{:=^30}'.format (''))
num = int(input('Informe o termo da PA: '))
raz = int(input('Informe a razão da PA: '))
print('')
lim = num + (10 - 1) * raz
for c in range(num, lim, raz):
    print('{}'.format(c))
print('')
print('{:=^30}'.format (''))
print('')