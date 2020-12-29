#!/usr/bin/env python
# Exercicio 3.6 - Escreva uma expressão que será utilizada para saber se um aluno sera aprovado ou não. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.
print ('    ')
nome = input('Informe o nome do Aluno: ')
print ('    ')
materia1 = float(input('Informe a nota da 1° Matéria: '))
materia2 = float(input('Informe a nota da 2° Matéria: '))
materia3 = float(input('Informe a nota da 3° Matéria: '))
# Tirando a media de das materias
med = ( materia1 + materia2 + materia3 ) / 3
print ('    ')
print (f'O Aluno {nome}, obteve ás seguintes notas em Ciencias {materia1}, em Matématica {materia2} e em Ingles {materia3} sua média geral foi {med:2.2f}') 
print ('    ')
if med > 7:
    print(f'Parabés Sr(a) {nome} você foi Aprovado!')
else:
    print(f'Infelizmente o Sr(a) {nome} não atigiu a nota para Aprovação.')
print ('    ')
