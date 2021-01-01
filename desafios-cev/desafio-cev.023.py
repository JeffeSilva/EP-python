#!/usr/bin/env python
num = str(input('Informe um numero entre 0 e 9999: '))
div = num.split()
print('Unidade:', div[0][3])
print('Dezena:', div[0][2])
print('Centena:', div[0][1])
print('Milhar:', div[0][0])
