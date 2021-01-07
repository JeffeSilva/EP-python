#!/usr/bin/env python
print('{:=^40}'.format (' Somente N° Pares de 1 até 50 '))
for c in range(1, 50+1):    
    if c % 2 == 0:
        print(c)
print('{:=^20}'.format('Fim'))