#!/usr/bin/env python
print (' ')
print ('Usando até a presente aula do curso em video')
n = int(input('Informe um número: '))
print (' ')
print (f'{n} x 1 =', n * 1)
print (f'{n} x 2 =', n * 2)
print (f'{n} x 3 =', n * 3)
print (f'{n} x 4 =', n * 4)
print (f'{n} x 5 =', n * 5)
print (f'{n} x 6 =', n * 6)
print (f'{n} x 7 =', n * 7)
print (f'{n} x 8 =', n * 8)
print (f'{n} x 9 =', n * 9)
print (f'{n} x 10 =', n * 10)
print (' ')
print ('Agora tentando usar estrutura de repetição cap-5 do livro')

n1 = int(input('Informe de qual numero deseja a tabuada: '))
fim = int(input('Informe até qual valor quer a tabuada: '))
x = 1
while x <= fim:
	r = n1 * x
	print (f'{n1} x {x} = {r}') 
	x = x + 1
print (' ')
print ('SEMPRE VERIFICAR A ORDEM OS FATORES TANTO DA IMPRESSÃO QUANTO DA ESTRUTURA DE REPETIÇÃO EM SI POIS NESSES CASOS A ADIÇÃO DE +1 AO X ATRAPALHO O RESULTADO - POREM COM A IMPRESSÃO ANTES DA ADIÇÃO DE X = X + 1 DEU TUDO CERTO!')
print (' ')
