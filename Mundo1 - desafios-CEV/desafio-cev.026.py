#!/usr/bin/env python
print(' ')
frase = str(input('Digite uma frase: ')).strip().lower()
print(' ')
qvap = frase.count('a')
pa = frase.find('a')+1
ua = frase.rfind('a')+1
print(f'Na frase: {frase} \n\nAparece {qvap}(a)\nO primeiro aparece na possição: {pa} \nE o ultimo na posição: {ua}\n')
