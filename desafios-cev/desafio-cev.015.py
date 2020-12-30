#!/usr/bin/env python
print (' ')
dias = int(input('Informe o N° de dias: '))
km = float(input('Informe o N° de Km rodado: '))
pago = (dias * 60) + (km * 0.15)
print (f'O aluguel foi por {dias}dias, e rodou {km}Km o total a ser pago é: R${pago:.2f}')
print (' ')
