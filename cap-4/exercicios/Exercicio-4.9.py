#!/usr/bin/env python
# Exercicio 4.9 - Escreva um programa para aprovar o empréstimo  bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo numero de meses a pagar.
print ('    ')
imovel = int(input('Informe o valor do imóvel: '))
sal = float(input('Informe o salário bruto mensal: '))
tempo = int(input('Em quanto tempo pretende quitar o emprestimo. (Min 15 Max 30 Anos): '))
basesal = sal
baseimovel = imovel
print ('    ')
# Variaveis de Aptidão para adquiri emprestimo
prazo = tempo * 12
vpar = imovel / prazo
limitesal = basesal * 0.3
print ('    ')
# condições para adquirir
if vpar > limitesal:
	print ('Verifique o prazo, caso esteja no limite de 30 anos e recomendado que diminua o valor do imóvel caso contrario não podera adquirir este empréstimio')
elif vpar < limitesal:
	print ('Verifique as condições, pode reduzir a parcela aumentando o prazo e/ou com um imóvel de menor valor')
else:
	print ('Infelizmente você não tem capacidade financeira para adquirir este empréstimo')
print ('    ')
print (f'Seu salário é: R${sal:6.2f}')
print (f'Valor do imóvel: {imovel}')
print (f'Prazo em anos: {tempo}')
print (f'Prazo em meses: {prazo}')
print (f'Valor da parcela: R${vpar:6.2f}')
print ('    ')

