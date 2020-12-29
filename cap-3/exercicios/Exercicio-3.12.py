#!/usr/bin/env python
# Exercicio 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
print('    ')
dist = int(input('Informe a distancia da viagem em KM: '))
velm = int(input('Informe a velocidade média das estradas Km/h: '))
print('    ')
# Calculo
tvia = dist / velm
print('    ')
print(f'A distancia da viagem é {dist}Km, a velocidade média das estradas é de {velm}Km/h a viagem levara em media {tvia:5.2f}')
print('    ')

