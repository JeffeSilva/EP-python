#!/usr/bin/env python
print(' ')
tab = int(input('Informe qual tabuada você deseja: '))
fim = int(input('Informe até qual valor deseja taboada: '))
print(' ')
print('{:=^20}'.format (' Taboada do {} ').format(tab))
print(' ')
for c in range(1, fim+1):
    res = tab * c
    print('{} x {:2} = {}'.format(tab, c, res))
print(' ')
print('{:=^20}'.format (' FIM '))

# Bom o meu ficou um pouco diferente, porem com mais uma funcionalidade. o Usuario escolhe a taboada que ele quer e até o número que ele quer!.
