#!/usr/bin/env python
# Exercicio 3.15 - Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele ja fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro e calcule quantos dias de vida um fumante perdera. Exiba o total em dias.
print('    ')
qcfp = int(input('Informe a quantidade de cigarros que fuma em média por dia: '))
qtjf = int(input('Informe a quanto tempo você e fumante: '))
# Calculo para determinar N° de cigarros e o Tempo perdido
qcf = qcfp * 365
tcft = qcf * qtjf
tdvr = tcft * 10
ndr = tdvr / 1440
print('    ')
print(f'Você fuma a {qtjf} Anos, e fuma {qcfp} por dia. Você teve uma redução de{ndr:5.0f} dias de vida.')
print('    ')
