#!/usr/bin/env python
# Programa 4.5 - Conta de telefone com três faixas de preço.
print ('    ')
minutos = int(input('Quantos minutos você utilizou este mês: '))
#Condições
if minutos < 200:
    preço = 0.20
else:
    if minutos < 400:
        preço = 0.18
    else:
        preço = 0.15
print ('    ')
print (f'Você vai pagar este mês: R${minutos * preço:6.2f}')
print ('    ')
