#!/usr/bin/env python
print(' ')
print('{:=^30}'.format (''))
print(' ')
valores = 0
cont = 0
for c in range(1, 7):
    num = int(input('Informe {}° valores: '.format(c)))
    if num % 2 == 0:
        cont = cont + 1
        valores = valores + num
print(' ')
print('A soma dos {} valores PARES, é: {}'.format(cont, valores))
print(' ')
print('{:=^30}'.format (''))

# Consegui fazer este exercicio sem problemas, porem so vi que avia feito ao contrario na resolução em video, então resolvi com uma mudança. no if num % 2 == 0, agora if num % 2 == 1, <- ele desconsidera os impares e soma os pares, quando for if num % 2 == 0, ignora os pares e soma os impares.