#!/usr/bin/env python
print('')
num = int(input('Digite o número a fatorar: '))
print('')
base = num
res = 0
if base == num:
    base -= 1
    res = num * base
    while base != 1:
        base -= 1
        res = res * base
    print('O número {} fatorado é {}.'.format(num, res))
print('')
print('FIM DO PROGRAMA ')