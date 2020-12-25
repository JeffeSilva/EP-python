# Exercicio 3.13 - Escreva um programa que converta uma remperatura difitada em °C em °F. A formula para essa conversão é °F = 9 x °C / 5 + 32
print('    ')
temc = int(input('Informe a temperatura em °C: '))
#Conversão
temf = ( 9 * temc ) / 5 + 32
print('    ')
print(f'A temperatura em Graus Celcius é {temc}°C que em Fahrenheit é {temf}°F') 
print('    ')
