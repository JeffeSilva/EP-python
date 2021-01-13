#!/usr/bin/env python
#ENTRADA DO USUARIO
print('')
num = int(input('Informe o valor da progressão: '))
raz = int(input('Informe a razão da progressão: '))
print('')
res = num
c = 2
nl = 10
total = 0
print('A P.A de {} pela razão {} seu º valor é: {}'.format(num, raz, num), end=' -> ')
while nl != 0:
    total = total + nl
    while c <= total:
        res += raz
        c += 1
        print(res, end=' -> ')
    print('PAUSA ')
    nl = int(input('Quantos termos a mais deseja mostrar: '))
print('O programa foi conluido, e apresentou {} termos.'.format(total))
print('FIM ')
