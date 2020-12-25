# Exercicio 3.10 - Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
print('    ')
sal = float(input('Informe seu salário: '))
aum = float(input('Informe a porcentagem de aumento do salário: '))
print('    ')
# Calculo
salaum = sal + (sal * aum / 100)
vaum = sal * aum / 100
print('    ')
print(f'O salário anterior é: {sal}')
print(f'O valor do aumento é: {vaum}')
print(f'O salário com o aumento é: {salaum}')
print('    ')
