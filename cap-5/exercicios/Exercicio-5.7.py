#!/usr/bin/env python
# Exercicio 5.7 - Modifique o programa anterior de forma que o usuario tambem digite o inicio e o fim da tabuada, em vez de começar com 1 e 10.
print(' ')
print('{:=^35}'.format (' Tabuada '))
tabuada = int(input('Tabuada do: '))
fim = int(input('Até quanto deseja a tabuada: '))
print('{:=^35}'.format (''))
print(' ')
cont = 1
while cont <= fim:
    print('{} x {:2} = '.format(tabuada, cont), (tabuada * cont))
    cont += 1
print(' ')
print('{:=^35}'.format (' FIM '))
print(' ')
