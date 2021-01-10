#!/usr/bin/env python
# Exercicio 5.6 - Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1=2 etc.
print(' ')
print('{:=^20}'.format (' Tabuada '))
n = int(input('Tabuada de: '))
print('{:=^20}'.format (''))
print(' ')
x = 1
while x <= 10:
    print('{} x {:2} = '.format(n, x), n * x)
    x = x + 1
print(' ')
print('{:=^20}'.format (' FIM '))