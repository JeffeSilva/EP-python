#!/usr/bin/env python
# Variaveis Globais
mes = 1
# Entrada do Usuario
dep = float(input('Informe o valor do deposito: '))
tdj = float(input('Informe o valor da taxa (Ex. 3 = 3%): '))
ganho = dep
# Logica do programa
while mes < 25:
    ganho += (ganho * (tdj / 100))
    print(f'Saldo no {mes:2}° = R$ {ganho:6.2f}')
    mes += 1
print(f'Valor ganho total no periodo de 24 meses: R$ {ganho-dep:.2f}')
