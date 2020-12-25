# Exercicio 3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuario. Calcule o total em segundos.
print('    ')
dia = int(input('Informe N° em dias: '))
hora = int(input('Informe N° em Horas: '))
minuto = int(input('Informe N° em Minutos: '))
segundos = int(input('Informe N° em Segundos: '))
# Convertendo
dias = dia * 86400
horas = hora * 3600
minutos = minuto * 60
#Somando Total
totals = dias + horas + minutos + segundos
print(f'O total de {dia}dia, {hora}h, {minuto}min e {segundos}seg convertidos somente em segundos é igual á {totals}')
print('    ')
