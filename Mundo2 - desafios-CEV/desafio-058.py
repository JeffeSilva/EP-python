#!/usr/bin/env python
# COMPUTADOR RAMDOMIZA UM NÚMERO ENTRE 0 e 10!
from random import randint
computador = randint(0, 10)
#ENTRADA DE PALPITES DO USUARIO
tdt = 0
print('')
print('{:=^30}'.format (' Jogo da Adivinhação '))
num = int(input('Qual é o seu palpite de 0 a 10: '))
if num != computador:
    print('Errou tente denovo!')
    tdt += 1
    while num != computador:
        num = int(input('Tente novamente: '))
        tdt += 1
        #DICAS PARA USUARIO SABER SE É MAIOR OU MENOR DO QUE O PALPITE ANTERIOR!
        if computador > num:
            print('Errou, o valor é maior!')
        else:
            print('Errou, o valor é menor!')
    print('Parabéns, você acertou com {} tentativas e o número era {}.'.format(tdt, computador))
    print('')
