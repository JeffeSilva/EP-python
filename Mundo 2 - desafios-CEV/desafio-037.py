#!/usr/bin/env python
from time import sleep
#PRIMEIRO IMPUT DO USUARIO, ESCOLHENDO UM NÚMERO PARA CONVERSÃO
print(' ')
num = int(input('Informe um número: '))
base = num
print('PROCESSANDO...')
sleep(2)
#MENU PARA USUARIO ESCOLHER QUAL CONVERSÃO ELE QUER FAZER
print(' ')
print('Escolha o número correspondente a base deseja a conversão: (1) BINARIO - (2) OCTAL - (3) HEXADECIMAL')
bqc = int(input('DIGITE O NÚMERO: '))
print('PROCESSANDO...')
sleep(2)
#CONVERSÃO E IMPRESSÃO
print(' ')
if bqc == 1:
    bina = bin(num)
    print('O número {} convertido em Binario é: {}.'.format(base, bina[2:]))
elif bqc == 2:
    octo = oct(num)
    print('O número {} convertido em Octal é: {}.'.format(base, octo[2:]))
elif bqc == 3:
    rex = hex(num)
    print('O número {} convertido em Hexadecimal é: {}.'.format(base, rex[2:]))
else:
    print('Informação invalida')

