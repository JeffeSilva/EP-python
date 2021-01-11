#!/usr/bin/env python
print('')
print('{:=^40}'.format (' Verificador de Palindromo '))
frase = str(input('Digite uma frase: ')).strip().upper()
base = frase.split()
junto = ''.join(base)
invertido = ''
print('{:=^40}'.format (''))
print('')
for letra in range(len(junto) -1, -1, -1):
    invertido += junto[letra]
if invertido == junto:
    print('A frase {} é um palindromo!'.format(frase))
else:
    print('A frase {} não é um palindromo!'.format(frase))
print(junto, invertido)
print('')
print('{:=^40}'.format (' FIM '))
print('')