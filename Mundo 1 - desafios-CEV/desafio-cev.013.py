#!/usr/bin/env python
# Desafio 013 - Faça um algoritmo que leia o salario de um funcionario e de um aumento de 15%, mostre o antigo, o novo e quanto foi o aumento.
print (' ')
sal = float(input('Informe o valor do salario: '))
print (' ')
aum = 0.15
qfaum = sal * aum
aumsal = qfaum + sal
print (f'O seu salário é de R${sal}, com aumento seu atual salario é de R${aumsal:.2f} o valor que foi aumentado foi R${qfaum:.2f}')
print (' ')

