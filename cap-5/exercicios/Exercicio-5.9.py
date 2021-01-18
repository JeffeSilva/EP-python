#!/usr/bin/env python
# Variaveis Globais
c = 1
# Entrada do Usuario
n = int(input('Informe o valor a ser dividido: '))
n1 = n
n2 = int(input('Informe o valor que vai dividir: '))
# Logica do programa
while n != 0:
    n -= n2
    c += 1
print(f'{n1} / {n2} = {c - 1}')