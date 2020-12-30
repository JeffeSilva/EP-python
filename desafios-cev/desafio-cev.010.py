#!/usr/bin/env python
# Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem e quantos dolares ela pode comprar (Considere: US1,00 = R$3,27)
print (' ')
din = float(input('Informe quanto dinheiro tem: '))
vdol = 5.17
qdol = din / vdol
print (' ')
print (f'Você tem R${din:5.2f}, e pode comprar U${qdol:.2f}')
print (' ')
