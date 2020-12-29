#!/usr/bin/env python
# Exercicio 4.1 - Analise o programa 4.1 e responda o que acontece se o primeiro e o segundo valor forem iguais? Explique.
print('    ')
n1 = int(input('Informe o Primeiro Valor: '))
n2 = int(input('Informe o Segundo Valor: '))
# Condição
print('    ')
if n1 > n2:
    print('O primeiro valor e maior')
if n2 > n1:
    print('O segundo valor e maior')
print('Explicação: Se ambos os numeros forem iguais, não apresentara nenhum dos resultados pois não existe condição que avalie esta situação como por exemplo >=, <=, == ou != pois na situação presente estamos utilizando os operadores relacionais')
print('    ')

