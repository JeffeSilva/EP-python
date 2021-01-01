#!/usr/bin/env python
from random import shuffle
print (' ')
alu1 = str(input('Informe o nome do aluno(a): '))
alu2 = str(input('Informe o nome do aluno(a): '))
alu3 = str(input('Informe o nome do aluno(a): '))
alu4 = str(input('Informe o nome do aluno(a): '))
print (' ')
lista = [alu1, alu2, alu3, alu4]
shuffle(lista)
print (f'A ordem de apresentação dos trabalhos é: {lista}')
print (' ')