#!/usr/bin/env python
import random
print (' ')
alu1 = str(input('Informe o nome do aluno(a): '))
alu2 = str(input('Informe o nome do aluno(a): '))
alu3 = str(input('Informe o nome do aluno(a): '))
alu4 = str(input('Informe o nome do aluno(a): '))
print (' ')
lista = [alu1, alu2, alu3, alu4]
random.shuffle(lista)
print (f'A ordem de apresentação dos trabalhos é: {lista}')
print (' ')