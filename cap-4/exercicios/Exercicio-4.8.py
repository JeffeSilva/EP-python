#!/usr/bin/env python
# Exercicio 4.8 - Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular Soma (+), Subtração (-), Multiplicação (*) e Divisão (/). Exiba o resultado da operação solicitada.
print ('    ')
n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
ope = input('Qual operação você deseja realizar: ')
print ('    ')
# Estrutura e condição
if ope == '+':
	res = n1 + n2
elif ope == '-':
	res = n1 - n2
elif ope == '*':
	res = n1 * n2
elif ope == '/':
	res = n1 / n2
else:
	print('Operação invalida, Informe a operação!')
	res = 0
print (f'Os valores informados são {n1}, {n2} e o resultado é {res:6.2f}.')
print ('    ')
