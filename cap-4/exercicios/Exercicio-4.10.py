# Exercicio 4.10 - Esreva um programa que calcule o preço a pagar pelo fornecimento de enerfia elétrica. pergunte a quantidade de kWh comnsumida e o tipo de instalação: R para residências, I para indústriais e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
print ('    ')
tipo = input('Informe a tipo R - Residencial, C - Comercial ou I - Industrial: ')
kwh = int(input('Informe a quantidade de kWh consumido na instalação: '))
print ('    ')
# Reparei que não e tão necessario infeitar o pavão então vamos la
if tipo == 'R' and kwh <= 500:
	preço = kwh * 0.40
elif tipo == 'R' and kwh > 500:
	preço = kwh * 0.65
elif tipo == 'C' and kwh <= 1000:
	preço = kwh * 0.55
elif tipo == 'C' and kwh > 1000:
	preço = kwh * 0.60
elif tipo == 'I' and kwh <= 5000:
	preço = kwh * 0.55
elif tipo == 'I' and kwh > 5000:
	preço = kwh * 0.60
else:
	print ('Verifique se selecionou o tipo correto, caso contrario execute novamente o programa!.')
	preço = 0
print (f'O consumo da instalação é: R${kwh:4.2f}')
print (f'O valor total a ser pago é: R${preço:6.2f}')
print ('    ')
