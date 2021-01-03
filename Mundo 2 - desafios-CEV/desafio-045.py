#!/usr/bin/env python
from time import sleep
from random import randint
# Menu e interação com jogador!
print(' ')
print('Olá eu sou o computador, gostaria de jogar uma partida de jokenpo?')
print('Eu também posso simular uma mão quer ver? bom, estou um pouco desatualizado mais enfim quer jogar?')
print(' ')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('-=                   |                    |                    =-')
print('-=    (1) - PEDRA    |    (2) - PAPEL     |   (3) - TESOURA    =-')
print('-=                   |                    |                    =-')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(' ')
jdu = int(input('Para fazer sua jogada escolha o número correspondente: '))
print(' ')
sleep(1)
print('[ JO ]')
sleep(1)
print('[ KEN ]')
sleep(1)
print('[ PO ]')
# Joagada do Computador
jdpc = int(randint(1, 3))
print(' ')
# Regras de negocio - Estrutura do jogo em if, elif e else
if jdu == 1 and jdpc == 2:
    print('Computador {} - PAPEL - \nJogador {} - PEDRA - \n\nEU VENCI!'.format(jdpc, jdu))
elif jdu == 2 and jdpc == 3:
    print('Computador {} - TESOURA - \nJogador {} - PAPEL - \n\nEU VENCI!'.format(jdpc, jdu))
elif jdu == 3 and jdpc == 1:
    print('Computador {} - PEDRA - \nJogador {} - TESOURA - \n\nEU VENCI!'.format(jdpc, jdu))
elif jdpc == 1 and jdu == 2:
    print('Jogador {} - PAPEL - \nComputador {} - PEDRA - \n\nVOCÊ É O VENCEDOR -.-'.format(jdu, jdpc))
elif jdpc == 2 and jdu == 3:
    print('Jogador {} - TESOURA - \nComputador {} - PAPEL -  \n\nVOCÊ É O VENCEDOR -.-'.format(jdu, jdpc))
elif jdpc == 3 and jdu == 1:
    print('Jogador {} - PEDRA - \nComputador {} - TESOURA - \n\nVOCÊ É O VENCEDOR -.-'.format(jdu, jdpc))
elif jdpc == jdu:
    print('Empate! você é bom mesmo.')
else:
    print('Erro 01 - verifique e tente novamente!')
