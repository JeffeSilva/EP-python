#!/usr/bin/env python
print('')
num = int(input('Informe o valor da progressão: '))
raz = int(input('Informe a razão da progressão: '))
print('')
res = num
c = 1
print('A P.A de {} pela razão {} seu º valor é: {}'.format(num, raz, num), end=' -> ')
while c != 10:
    res += raz
    c += 1
    print(res, end=' -> ')
print('FIM ')
print('')