#!/usr/bin/env python
# Exercicio 5.7 - Modifique o programa anterior de forma que o usuario tambem digite o inicio e o fim da tabuada, em vez de começar com 1 e 10.
inicio = int(input('Digite o número que deseja começar: '))
fim = int(input('Digite o número que deseja terminar: '))
while inicio <= fim:
    print('{} x {} = '.format(inicio, fim), (inicio * fim))
    inicio += 1
