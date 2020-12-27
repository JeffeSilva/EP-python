# Programa 4.6 - Categoria x Preço
print ('    ')
categoria = int(input('Digite a categoria do produto: '))
print ('    ')
# Condições
if categoria == 1:
	preço = 10
else:
	if categoria == 2:
		preço = 18
	else:
		if categoria == 3:
			preço = 23
		else:
			if categoria == 4:
				preço = 26
			else:
				if categoria == 5:
					preço = 31
				else:
					print('Categoria invalida, digite um valor entre 1 e 5!')
					preço = 0
print (f'O preço do produto é: R${preço:6.2f}')
print ('    ')
