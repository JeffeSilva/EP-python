#!/usr/bin/env python
soma = 0
cont = 0
for c in range(1, 500+1):
    if c % 3 == 0 and c % 2 == 1:
        cont = cont + 1
        soma = soma + c
print(' ')
print('{:=^20}'.format (' Ex. 048 '))
print('A soma de todos os {} números impares multiplos de 3 entre 1 e 500 é:{}'.format(cont, soma))
print('{:=^20}'.format (' FIM '))

#Neste programa foi implementado o conceito de acumulador, ele serve para "JUNTAR, ACUMULAR E/OU (SALVAR O VALOR ANTERIOR DA VARIAVEL X)" fazendo com que seja possivel somar varios números dentro de uma estrutura de repetição.

#O conceito de contador tambem foi explicado assim como no livro, "x = x + 1" essa expressão vai nos mostrar quantas vezes foi adicionado o número ao acumulador por exemplo.
