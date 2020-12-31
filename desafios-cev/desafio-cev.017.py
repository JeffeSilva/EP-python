#!/usr/bin/env python
from math import sqrt
print (' ')
cato = float(input('Informe comprimento do cateto oposto: '))
cata = float(input('Informe comprimento do cateto adjacente: '))
print (' ')
sqdc = (cato ** 2) + (cata ** 2)
hipo = sqrt(sqdc)
print (f'Cateto Oposto = {cato:.2f} \nCateto Adjacente = {cata:.2f} \nHipotenusa {hipo:.2f}')
print (' ')