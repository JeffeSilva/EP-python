#!/usr/bin/env python
from time import sleep
#variaveis
somatg = 0
mil = 0
maisbarato = 0
c = 1
nomemaisbarato = ''
while True:
    #Entrada dos dados pelo usuario
    nomep = str(input('Nome do produto: '))
    qualvdp = float(input('Valor do produto: '))
    sair = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    #Logica do programa
    if qualvdp != 0:
        somatg += qualvdp
    if qualvdp > 1000.00:
        mil += 1
    if c == 1:
        maisbarato = qualvdp
    else:
        if qualvdp < maisbarato:
            maisbarato = qualvdp
            nomemaisbarato = nomep
    if sair != 'S':
        print('PROCESSANDO...')
        sleep(2)
        break
    c += 1
print('O valor total gasto foi de: R$ {:.2f}\n{} Produtos custam mais de mil reais\nO produto mais barato é {} e custa R$ {:.2f}.'.format(somatg, mil, nomemaisbarato, maisbarato))
