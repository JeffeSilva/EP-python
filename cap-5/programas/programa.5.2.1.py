#!/usr/bin/env python
# Programa 5.2.1 - Ultimo número informado pelo usuario, imrpimindo somente os números pares
print(' ')
fim = int(input('Digite o último número a imprimir: '))
x = 0
while x <= fim:
    print('.', end=' ')
    if x % 2 == 0:
        print(x)
    x = x + 1
print(' ')
print('FIM ')

#PROGRAMA REPETINDO USANDO MENOS REPETIÇÕES, OTIMIZADO COMO NO CURSO EM VIDEO!

# O PROGRAMA ABAIXO REPETE 6 VEZES O LAÇO OTIMIZANDO O PROGRAMA ACIMA -"OBSERVE QUE O RESULTADO E O MESMO POREM USA 50% A MENOS O PROCESSAMENTO" BASTA ACOMPANHAR OS PONTOS ANTES DOS NÚMEROS

print(' ')
fim1 = int(input('Digite o ultimo número a imprimir: '))
print(' ')
x = 0
while x <= fim:
    print('.', end=' ')
    print(x)
    x = x + 2
print(' ')
print('FIM ')

