#!/usr/bin/env python
# Programa 4.7 - Categoria x Preço, usando elif
print ('    ')
categoria = int(input('Digite a categoria do produto: '))
print ('    ')
# Condições.
if categoria == 1:
	preço = 10
elif categoria == 2:
	preço = 18
elif categoria == 3:
	preço = 23
elif categoria == 4:
	preço = 26
elif categoria == 5:
	preço = 31
else:
	print ('Categoria inválida, digite um valor entre 1 e 5!')
	preço = 0
print (f'O preço do produto é: R${preço:6.2f}')
print ('    ')
