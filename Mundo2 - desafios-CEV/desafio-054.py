#!/usr/bin/env python
from datetime import date
menores = 0
maiores = 0
print('{:=^45}'.format (' TESTE DE IDADE '))
for c in range(1, 7 + 1):
    print('')
    data = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    print('')
    if date.today().year - data <  21:
        menores += 1
    else:
        maiores += 1
print('({}) pessoas são menores \n({}) pessoas são maiores'.format(menores, maiores))
print('')
print('{:=^45}'.format (''))
print('')

