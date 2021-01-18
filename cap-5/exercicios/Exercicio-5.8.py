#!/usr/bin/env python
#Variaveis Globais
c = 0
ac = 0
#Entrada do Usuario
print('')
n1 = int(input('Informe um valor: '))
n2 = int(input('Informe outro valor: '))
#Logica do programa
while c < n2:
    ac += n1
    c += 1
print('')
print(f'{n1} x {n2} =', (ac))
print('')
print('FIM ')
