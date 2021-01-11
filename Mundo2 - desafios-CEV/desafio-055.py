#!/usr/bin/env python
print('')
menor = 0
maior = 0
print('{:=^30}'.format (' Qual o mais pesado '))
print('')
for c in range(1, 5 + 1):
    peso = float(input('Peso da {}° pessoa: '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('')
print('O menor peso lido foi: {} Kg \nO maior peso lido foi: {} Kg'.format(menor, maior))
print('')
print('{:=^30}'.format (' FIM '))