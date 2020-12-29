#!/usr/bin/env python
# Exercicio 3.14 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
print('    ')
dia = int(input('Informe o N° de dias que o carro foi Alugado: '))
kmp = int(input('Informe a quantidade de Km rodados com veiculo enquanto alugado: '))
print('    ')
# Calculo
vdia = 60.00
vkm = 0.15
vapd = dia * vdia
vapk = kmp * vkm
vtap = vapd + vapk
# Mostrar valores e dizeres ao cliente!
print(f'O veiculo foi alugado por {dia} dias, e percorreu {kmp}Km')
print(f'O valor a ser pago pelos dias alugados é R$ {vapd:5.2f}, e pelos Kilometros rodados é R${vapk:5.2f}')
print(f'O valor total a ser pago é de R$ {vtap:5.2f}')
print('    ')

