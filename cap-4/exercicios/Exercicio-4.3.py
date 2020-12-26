# Exercicio 4.3 - Escreva um programa que leia três números e que imprima o maior e o menor.
print ('    ')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
print ('    ')
# Condições para verificar valor maior
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
# Condição para verificar valor menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print ('    ')
print (f'O maior valor é: {maior}, e o menor valor é: {menor}.')
