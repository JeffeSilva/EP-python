#!/usr/bin/env python
print(' ')
tab = int(input('Informe qual tabuada você deseja: '))
fim = int(input('Informe até qual valor deseja taboada: '))
print(' ')
print('{:=^20}'.format (' Taboada {} ').format(tab))
print(' ')
for c in range(1, fim+1):
    res = tab * c
    print('{} x {:2} = {}'.format(tab, c, res))
print(' ')
print('{:=^20}'.format (' FIM '))