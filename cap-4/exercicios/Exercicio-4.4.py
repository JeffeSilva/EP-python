#!/usr/bin/env python
# Exercicio 4.4 - Escreva um programa que pergunte o salario do funcionario e calcule o valor do aumento. Para salarios superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
print('    ')
sal = float(input('Informe seu salário: '))
salaum = 0
aum1 = 10
aum2 = 15
print ('    ')
if sal <= 1250.00:
    salaum = sal + (sal * aum2) / 100
if sal > 1250.00:
    salaum = sal + (sal * aum1) / 100
valorau = salaum - sal
print (f'Seu salário é: R$ {sal}, e teve um aumento de R$ {valorau} atualmente seu salario é: R$ {salaum}.')
print ('    ')
