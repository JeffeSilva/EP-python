#!/usr/bin/env python
# Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
print (' ')
prod = float(input('Informe o valor do produto: '))
print (' ')
desc = prod * 0.05
vpcd = prod - desc
print (f'O produto custa R${prod:.2f} e obteve um desconto de 5%, R${desc:.2f} o valor atual do produto é: R${vpcd:.2f}')
print (' ')

