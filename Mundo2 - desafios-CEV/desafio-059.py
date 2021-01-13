#!/usr/bin/env python
from time import sleep
#VARIAVEIS DO PROGRAMA
menu = 0
res = 0
#Entrada do 1º e 2º número
print('')
n1 = int(input('Informe um valor: '))
n2 = int(input('Informe outro valor: '))
print('')
#Menu de interação
while menu != 5:
    print('{:=^30}'.format (' MENU '))
    print('= [ 01 ] - SOMAR             =')
    print('= [ 02 ] - MULTIPLICAR       =')
    print('= [ 03 ] - MAIOR             =')
    print('= [ 04 ] - NOVOS NÚMEROS     =')
    print('= [ 05 ] - SAIR DO PROGRAMA  =')
    print('{:=^30}'.format (''))
    print('')
    #Entrada de comando no menu
    menu = int(input('Qual operação deseja realizar?: '))
    if menu == 1:
        res = n1 + n2
        print('A soma de {} e {} é igual a {}.'.format(n1, n2, res))
    elif menu == 2:
        res = n1 * n2
        print('A multiplicação de {} e {} é igual a {}.'.format(n1, n2, res))
    elif menu == 3:
        if n1 > n2:
            print('O maior valor entre {} e {} é {}.'.format(n1, n2, n1))
        else:
            print('O maior valor entre {} e {} é {}.'.format(n1, n2, n2))
    elif menu == 4:
        n1 = int(input('Informe o 1° número: '))
        n2 = int(input('Informe o 2° número: '))
    else:
        print('Opção Invalida, verifique e tente novamente!')
if menu == 5:
    print('Finalizando...')
    sleep(2)
print('')
print('Obrigado por utilizar nosso programa. Volte sempre!')
print('')


