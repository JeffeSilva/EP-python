#!/usr/bin/env python
print(' ')
frase = str(input('Digite uma frase: '))
print(' ')
qvap = frase.lower().count('a')
pa = frase.find('a')
ua = frase.rfind('a')
print(f'Na frase: {frase} \n\nAparece {qvap}(a)\nO primeiro aparece na possição: {pa} \nE o ultimo na posição: {ua}\n')
