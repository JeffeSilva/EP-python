#!/usr/bin/env python
#O USUARIO ENTRA COM OS VALORES
print(' ')
n1 = int(input('Informeu um número: '))
n2 = int(input('Informe outro número: '))
#INICIA OS TESTES DOS NÚMEROS
print(' ')
if n1 == n2:
    print('Não existe valor maior, ambos são iguais!')
elif n1 > n2:
    print('O primeiro valor é maior!')
else:
    print('O segundo valor é maior')