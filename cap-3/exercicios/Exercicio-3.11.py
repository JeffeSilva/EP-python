# Exercicio 3.11 - Escreva um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
print('    ')
vpro = float(input('Informe o valor do produto: '))
vdes = float(input('Informe o valor do desconto: '))
print('    ')
# Calculo
prodes = vpro * vdes / 100
propag = vpro - prodes
print (f'O valor do produto informado é: R$ {vpro:5.2f}')
print (f'A porcentagem de desconto deste produto é: {vdes:2.2f}%')
print (f'Valor a ser descontado do produto: R$ {prodes:5.2f}')
print (f'Valor total a ser pago pelo produto: R$ {propag:5.2f}')
print('    ')

