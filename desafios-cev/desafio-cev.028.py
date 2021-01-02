#!/usr/bin/env python
from time import sleep
from random import choice
print(' ')
print('Quer jogar? \nVou pensar em um número entre 0 e 5. \nse você acertar você vence!')
print(' ')
num = int(choice([0, 1, 2, 3, 4, 5]))
tdu = int(input('Qual número você acha que é: '))
print('CARREGANDO...')
sleep(3)
if num == tdu:
    print('Parabéns você venceu!')
else:
    print('Você errou, eu venci!')
print('O número foi {}'.format(num))
print(' ')
