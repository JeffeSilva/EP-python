#!/usr/bin/env python
from random import choice
print (' ')
alu1 = str(input('Informe o nome do 1° Aluno: '))
alu2 = str(input('Informe o nome do 2° Aluno: '))
alu3 = str(input('Informe o nome do 3° Aluno: '))
alu4 = str(input('Informe o nome do 4° Aluno: '))
print (' ')
sort = choice([alu1, alu2, alu3, alu4])
print (f'O aluno ou aluna sorteado para apagar o quadro é: {sort}!')
print (' ')