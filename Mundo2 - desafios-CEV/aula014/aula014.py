#!/usr/bin/env python
print('')
print('{:=^30}'.format (' AULA 014 - While PRATICA '))
print('')
for c in range(1, 10):
    print(c)
print('FIM ')
print('')
print('{:=^30}'.format (' TESTE 1 - CONTADORES '))
print('')
c = 1
while c < 10:
    print(c)
    c += 1
print('')
print('FIM ')
print('')
print('{:=^30}'.format (' TESTE 2 - ENTRADA DE DADOS '))
print('')

print('ESTE REPETE UM N° LIMITADO DE VEZES')
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('')
print('FIM ')
print('')
print('{:=^30}'.format (''))
print('')
print('ESTE REPETE ATÉ O USUARIO DIGITAR O COMANDO DE SAIR QUE È (0)')
n = 1
while n != 0: #<- Esse cara chama Flag (CONDIÇÃO DE PARADA)
    n = int(input('Digite um valor, ou (0) para sair: '))
print('')
print('FIM ') 
print('')
print('{:=^30}'.format (''))
print('')
print('PERGUNTA SE O USUARIO DESEJA CONTINUAR OU NÃO')
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('')
print('FIM ')
print('')
print('{:=^30}'.format (''))
print('')
print('{:=^30}'.format (' Teste de Par ou Impar '))
print('')
impar = 0
par = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
            if n == 0:
                n = 0
print('{} números pares \n{} números impares'.format(par, impar))